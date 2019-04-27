<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>个人信息</el-breadcrumb-item>
      <el-breadcrumb-item>修改头像</el-breadcrumb-item>
    </el-breadcrumb>
    <h3 class="start"><i class="el-icon-upload"></i>&nbsp;要更新您的头像吗，亲？</h3>
    <el-upload class="avatar-uploader"
               action="http://localhost:8000/api/upload_pic"
               :show-file-list="false"
               :on-success="handleAvatarSuccess"
               :before-upload="beforeAvatarUpload"
               >
      <img v-if="imageUrl"
           :src="imageUrl"
           class="avatar"
           style="border-radius:100px">
      <i v-else
         class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>

    <el-form :model="form"
             v-show="imageUrl!=''? true:false"
             ref="uploadform"
             label-width="100px"
             class="uploadform"
             style="margin-top:-100px">
      <h6>上传成功，点击图片仍然可以重新上传</h6>
      <el-form-item label=""
                    v-show="false"
                    prop="url">
        <el-input v-model="form.picture"></el-input>
      </el-form-item>
      <el-form-item style="margin-left:-90px;margin-top:-80px">
        <el-button type="primary"
                   @click="submitForm()">提交</el-button>
        <el-button @click="backMenu()">不换了，返回</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
export default {
  data () {
    return {
      imageUrl: '',
      form: {
        username: '',
        picture: ''
      }
    }
  },
  components: {

  },
  methods: {
    handleAvatarSuccess (res, file) {
      console.log(res)
      this.imageUrl = this.$store.state.base_url + res.url
      this.form.picture = res.url
      this.$message.success({
        title: '上传成功',
        message: '图片上传成功'
      })
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    submitForm () {
      let that = this
      that.form.username = that.$store.state.userinfo.username
      that.$confirm('确定要换头像吗，亲？', '换头像确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        that.$axios.put('/user/myself', that.form).then(res => {
          if (res.data.flag === 'success') {
            that.$message({
              type: 'success',
              message: '头像更新成功,会有缓存，可以刷新后查看'
            })
            that.$router.push('/personal')
          } else {
            that.$message({
              type: 'error',
              message: '上传失败'
            })
          }
        })
      }).catch(() => {
        that.$message({
          type: 'info',
          message: '取消换头像'
        })
      })
    },
    backMenu () {
      this.$router.push('/personal')
    }
  }
}
</script>

<style scoped>
.avatar-uploader .el-upload {
  border: 1px dashed black;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: black;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: black;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.start{
  margin-top: 150px
}
</style>
