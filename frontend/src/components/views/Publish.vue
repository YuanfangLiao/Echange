<template>
  <div class="page">

    <el-steps :active="active"
              finish-status="success">
      <el-step title="填写简单介绍"></el-step>
      <el-step title="填写详细信息"></el-step>
      <el-step title="确认信息并提交"></el-step>
    </el-steps>

    <br />
    <el-tag type="info"
            class="info-box"
            v-show="active === 0">
      <h1>Hi {{ username }},有什么闲置物品想换的吗，来这里发布吧～</h1>
    </el-tag>
    <h1>{{ titleMsg }}</h1>
    <el-form label-position="top"
             label-width="80px"
             :model="form">
      <el-form-item label="物品名称(标题)"
                    required
                    v-show="active === 0">
        <el-input v-model="form.title"
                  placeholder="物品简介(50字以内)"></el-input>
      </el-form-item>
      <el-form-item label="物品种类"
                    required
                    v-show="active === 0">
        <el-select v-model="form.type"
                   placeholder="请选择">
          <el-option v-for="item in options"
                     :key="item.value"
                     :label="item.label"
                     :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="你的估价(RMB)"
                    required
                    v-show="active === 0">
        <el-input v-model="form.price"
                  type="number"
                  placeholder="输入您的估价"></el-input>
      </el-form-item>
      <el-form-item label="品牌"
                    required
                    v-show="active === 0">
        <el-input v-model="form.brand"
                  placeholder="输入商品的品牌"></el-input>
      </el-form-item>
      <el-form-item label="新旧成色"
                    required
                    v-show="active === 0">
        <el-slider v-model="form.condition" :step="5"
                   :min="30"
                   show-input> </el-slider>
      </el-form-item>
      <el-form-item label="传几张图片吧"
                    required
                    v-show="active === 0">
        <el-upload action="http://localhost:8000/api/upload_pic"
                   list-type="picture-card"
                   :before-upload="handleBeforeUpload"
                   :on-success="handleSuccessUpload"
                   :on-error="handleErrorUpload"
                   :on-preview="handlePictureCardPreview"
                   :on-remove="handleRemove">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%"
               :src="dialogImageUrl"
               alt="">
        </el-dialog>
      </el-form-item>
      <el-form-item label="图片路径"
                    v-show="false">
        <el-input v-model="form.picture"
                  placeholder="图片路径"></el-input>
      </el-form-item>
      <el-form-item label="详细描述"
                    required
                    v-show="active === 1">
        <el-input v-model="form.detail"
                  type="textarea"
                  :rows="5"
                  placeholder="请输入您的宝贝的详细内容"></el-input>
      </el-form-item>
      <el-form-item label="期望换的物品"
                    required
                    v-show="active === 1">
        <el-input v-model="form.want"
                  type="textarea"
                  :rows="5"
                  placeholder="写一写你想换些啥"></el-input>
      </el-form-item>
    </el-form>
    <el-table :data="generateTable"
              stripe
              style="width: 100%"
              v-show="active === 2">
      <el-table-column prop="key"
                       label="属性">
      </el-table-column>
      <el-table-column prop="value"
                       label="值">
      </el-table-column>
    </el-table>
    <el-carousel :interval="4000"
                 type="card"
                 height="200px"
                 v-show="active === 2">
      <el-carousel-item v-for="item in this.form.picture.split('$$$').filter(item => item != '')"
                        :key="item">
        <img :src="baseUrl + item" width="100%">
        <!-- <h3>{{ baseUrl + item }}</h3> -->
      </el-carousel-item>
    </el-carousel>

    <el-button style="margin-top: 12px;"
               @click="last"
               v-show="active != 0">上一步</el-button>
    <el-button style="margin-top: 12px;"
               @click="next"
               v-show="active != 2">下一步</el-button>
    <el-button style="margin-top: 12px;"
               @click="submitForm"
               v-show="active == 2">提交</el-button>
  </div>
</template>

<script>
export default {
  name: 'Publish',
  data () {
    return {
      username: localStorage.getItem('username'),
      options: [],
      active: 0,
      dialogImageUrl: '',
      dialogVisible: false,
      myTitleMsg: '',
      baseUrl: this.$store.state.base_url,
      form: {
        title: '',
        type: '',
        price: '',
        brand: '',
        condition: 90,
        picture: '',
        detail: '',
        want: ''
      }
    }
  },
  computed: {
    generateTable: function () {
      let myOptions = {}
      for (let item of this.options) {
        myOptions[item.value] = item.label
      }
      return [
        {
          key: '物品简介',
          value: this.form.title },
        {
          key: '物品种类',
          value: myOptions[this.form.type]
        },
        {
          key: '价格',
          value: this.form.price
        },
        {
          key: '品牌',
          value: this.form.brand
        },
        {
          key: '新旧程度',
          value: this.form.condition + '成新'
        },
        {
          key: '详细信息',
          value: this.form.detail
        },
        {
          key: '想换的',
          value: this.form.want
        }
      ]
    },
    titleMsg: function () {
      if (this.active === 0) return '填写基本信息'
      else if (this.active === 1) return '描述一下你的宝贝，并说一下想要些什么'
      else return 'check一下信息，并发布吧'
    }
  },
  mounted () {
    let that = this
    that.$axios.get('/api/all_goods_type').then(res => {
      that.options = res.data.data
      console.log(that.options)
    })
  },
  methods: {
    submitForm () {
      let that = this
      this.$confirm('确定信息无误提交吗，亲？', '发布确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        that.$axios.post('/goods/goods', this.form).then(res => {
        // 发布成功
          if (res.data.flag === 'success') {
            this.$notify.success({title: '发布成功',
              message: '发布商品成功'})
            this.$router.push('/home')
          } else {
            this.$notify.error({title: '发布失败',
              message: res.data.error})
          }
        }).catch(err => {
          this.$notify.error({title: '发布失败',
            message: '发布商品失败'})
          console.log(err)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消发布'
        })
      })
    },
    last () {
      this.active--
    },
    next () {
      // title: '',
      // type: '',
      // price: '',
      // brand: '',
      if (this.active === 0) {
        let form = this.form
        if (form.title && form.type && form.price && form.brand && form.picture) this.active++
        else this.$message.warning('请填写必填项')
      } else if (this.active === 1) {
        let form = this.form
        if (form.detail && form.want) this.active++
        else this.$message.warning('请填写必填项')
      }
      // this.active++
    },
    // 删除图片的钩子
    handleRemove (file, fileList) {
      // 先告诉用户图片删除成功，然后再处理服务器，服务器对用户来说不重要
      let removeUrl = file.response.url + '$$$'
      let pictureUrl = this.form.picture
      pictureUrl = pictureUrl.replace(removeUrl, '')
      this.form.picture = pictureUrl
      this.$message.info({
        // title: '成功',
        message: '图片删除成功'
      })
      let that = this

      let params = that.$qs.stringify({
        url: file.response.url
      })
      // 开始删除服务器图片
      that.$axios.post('/api/del_pic', params).then(res => {
      }).catch(err => {
        console.log(err)
        // console.log(err)
      })
    },
    // 图片预览钩子
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    // 上传文件之前的钩子
    handleBeforeUpload (file) {
      console.log('before')
      if (!(file.type === 'image/png' || file.type === 'image/gif' || file.type === 'image/jpg' || file.type === 'image/jpeg')) {
        this.$message.warning({
          title: '警告',
          message: '请上传格式为image/png, image/gif, image/jpg, image/jpeg的图片'
        })
      }
      let size = file.size / 1024 / 1024 / 2
      if (size > 2) {
        this.$message.warning({
          title: '警告',
          message: '图片大小必须小于2M'
        })
      }
    },
    // 文件上传失败钩子
    handleErrorUpload (err, file, fileList) {
      this.$notify.error({
        title: '错误',
        message: '文件上传失败'
      })
      console.log(err)
    },
    // 文件上传成功钩子
    handleSuccessUpload (response, file, fileList) {
      this.form.picture += (response['url'] + '$$$')
      this.$message.success({
        title: '上传成功',
        message: '图片上传成功'
      })
    }
  },
  components: {

  }
}
</script>

<style scoped>
.page {
  width: 60%;
  margin: 0 auto;
}
.info-box {
  height: 60px;
}
</style>
