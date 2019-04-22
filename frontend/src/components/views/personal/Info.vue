<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>个人信息</el-breadcrumb-item>
      <el-breadcrumb-item>基本资料</el-breadcrumb-item>
    </el-breadcrumb>
    <h3><i class="el-icon-edit"></i>&nbsp;要更新您的资料吗，亲？</h3>
    <el-form :model="form"
             ref="form"
             label-width="80px"
             class="form"
             :rules="rules">
      <el-form-item label="用户名"
                    prop="username">
        <el-input v-model="form.username"
                  :disabled="!active"></el-input>
      </el-form-item>
      <el-form-item label="等级"
                    prop="level">
        <el-input v-model="form.level"
                  disabled></el-input>
      </el-form-item>
      <el-form-item label="个性签名"
                    prop="signature">
        <el-input v-model="form.signature"
                  :disabled="!active"
                  type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="您的地址"
                    prop="address">
        <el-input v-model="form.address"
                  :disabled="!active"></el-input>
      </el-form-item>
      <el-form-item label="性别"
                    prop="sex">
        <el-radio-group v-model="form.sex"
                        :disabled="!active">
          <el-radio :label="1">男</el-radio>
          <el-radio :label="2">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="手机号"
                    prop="address">
        <el-input v-model="form.phone"
                  :disabled="!active"></el-input>
      </el-form-item>
      <el-form-item label="您的邮箱"
                    prop="address">
        <el-input v-model="form.email"
                  :disabled="!active"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="warning"
                   :disabled="active"
                   v-if="!active"
                   @click="makeActive()">修改</el-button>
        <el-button type="primary"
                   v-if="active"
                   @click="submitForm()">提交</el-button>
        <el-button @click="disActive()"
                   v-if="active">取消</el-button>
      </el-form-item>
    </el-form>

  </div>
</template>

<script>
export default {
  data () {
    return {
      active: false,
      form: {
        username: '',
        level: '',
        phone: '',
        email: '',
        sex: '',
        address: '',
        signature: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        level: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        sex: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ],
        signature: [
          { required: true, message: '请输入必填项', trigger: 'blur' }
        ]
      }
    }
  },
  components: {

  },
  mounted () {
    this.$axios.get('/user/info').then(res => {
      this.form = res.data
    })
  },
  methods: {
    disActive () {
      this.active = false
    },
    makeActive () {
      this.active = true
    },
    submitForm () {
      let that = this
      this.$refs['form'].validate((valid) => {
        if (valid) {
          that.form.username = that.$store.state.userinfo.username
          that.$confirm('确定提交吗，亲？', '修改信息确认', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            that.$axios.put('/user/myself', that.form).then(res => {
              if (res.data.flag === 'success') {
                that.$message({
                  type: 'success',
                  message: '信息更新成功'
                })
                that.$router.push('/personal')
              } else {
                that.$message({
                  type: 'error',
                  message: '修改失败'
                })
              }
            })
          }).catch(() => {
            that.$message({
              type: 'info',
              message: '取消修改信息'
            })
          })
        } else {
          that.$message({
            type: 'error',
            message: '请按规则填写'
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.form {
  width: 500px;
  margin: 0 auto;
  text-align: left;
}
</style>
