<template>
  <div id="app">
    <router-view class="header" name="header"></router-view>
    <router-view class="content"></router-view>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
import MyFooter from './components/common/MyFooter'
import { timeFormat } from './assets/js/filters.js'
export default {
  name: 'App',
  components: {MyFooter},
  filters: {
    timeFormat
  }
}
</script>

<style>
.content{
  min-height: 800px;
  padding: 30px 50px;
}
body{
  margin: 0;
  padding: 0;
  /* min-height: 100%; */
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
body .el-table th.gutter {
  display: table-cell !important;
}

body .el-table colgroup.gutter {
  display: table-cell !important;
}
</style>
