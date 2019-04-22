<template>
  <el-row :gutter="20">
    <el-col :span="8">
      <div class="grid-content bg-purple">
        <img src="../../../../static/img/logo.jpg"
             width="250px" /></div>
    </el-col>
    <el-col :span="4">
      <div class="grid-content bg-purple"></div>
    </el-col>
    <el-col :span="12">
      <div class="grid-content bg-purple right-middle">
        <div v-if="checkuserpic"><img :src="getuserpic"
               width="80px"
               height="80px"
               class="user_img1"></div>
        <el-form :inline="true"
                 v-model="form"
                 class="form-inline">
          <el-form-item label="" prop="search">
            <el-input class="search-input"
                      v-model="form.search"
                      placeholder="搜索内容"
                      clearable></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
                       icon="el-icon-zoom-in"
                       round
                       @click="onSubmit">站内搜索</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  data () {
    return {
      input: '',
      form: {
        search: ''
      }
    }
  },
  name: 'myHeaderMiddle',
  methods: {
    onSubmit () {

    }
  },
  computed: {
    getuserpic: function () {
      // console.log('picaddress :' + this.$store.state.userinfo)
      if (this.checkuserpic === false) return ''
      else { return this.$store.state.base_url + this.$store.state.userinfo.picture }
    },
    checkuserpic: function () {
      let usr = this.$store.state.userinfo
      if (!usr || usr === undefined) return false
      else return true
    }
  }
}
</script>

<style>
.form-inline {
  padding-top: 50px;
}
.el-row {
  margin-bottom: 20px;
  height: 100px;
  vertical-align: middle;
  /* &:last-child {
      margin-bottom: 0;
    } */
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.search-input {
  width: 250px;
}
.right-middle {
  display: flex;
  flex-direction: row-reverse;
}
.user_img1 {
  margin: 30px;
  border-radius: 200px;
}
</style>
