<template>
  <el-row :gutter="20">
    <el-col :span="8">
      <div class="grid-content bg-purple">
        <img src="../../../static/img/logo.jpeg"
             width="250px" /></div>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple"></div>
    </el-col>
    <el-col :span="10">
      <div class="grid-content bg-purple">
        <el-form :inline="true"
                 class="form-inline">
          <el-form-item label="">
            <el-input class="search-input"
                      placeholder="搜索内容"
                      clearable></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
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
      input: ''
    }
  },
  name: 'myHeaderMiddle',
  methods: {
    onSubmit () {

    }
  },
  computed: {
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
</style>
