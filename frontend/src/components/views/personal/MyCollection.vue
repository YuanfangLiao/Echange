<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>换物中心</el-breadcrumb-item>
      <el-breadcrumb-item>我的收藏</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="my-table-display">
      <el-table :data="tableData"
                :show-header="true"
                style="width: 100%">

        <el-table-column prop="goods.title"
                         label="收藏内容"
                         width="380">
          <template slot-scope="scope">
            <div class="my-flex">
              <img :src="base_url + scope.row.goods.picture[0]"
                   alt=""
                   style="width: 80px;height: 80px">
              <div>{{ scope.row.goods.title }}</div>
            </div>
          </template>
        </el-table-column>
        <el-table-column prop="create_time"
                         label="收藏日期"
                         width="180">
          <template slot-scope="scope">
            {{ scope.row.create_time | timeFormat }}
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-tooltip class="item"
                        effect="dark"
                        content="点击查看收藏商品详情"
                        placement="top">
              <el-button type="primary"
                         @click="goGood(scope.row.goods.id)"
                         icon="el-icon-search"
                         circle></el-button>
            </el-tooltip>
            <el-tooltip class="item"
                        effect="dark"
                        content="点击删除收藏记录"
                        placement="top">
              <el-button type="danger"
                         @click="doDelete(scope.row.id,scope.$index,tableData)"
                         icon="el-icon-delete"
                         circle></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
// import { timeFormat } from '../../../assets/js/filters.js'
export default {
  data () {
    return {
      tableData: [],
      base_url: this.$store.state.base_url
    }
  },
  created () {
    this.$axios.get('/goods_api/collection', {
      params: {
        query: 'mine'
      }
    }).then(res => {
      this.tableData = res.data
    })
  },
  components: {

  },
  methods: {
    goGood (id) {
      this.$router.push(`/goods/${id}`)
    },
    doDelete (id, index, rows) {
      this.$confirm('确认取消收藏吗').then(() => {
        let that = this
        // let params = that.$qs.stringify({
        //   id: id
        // })
        console.log(id)
        that.$axios.delete('/goods_api/collection', { data: { id: id } }).then(res => {
          that.$message.success('删除成功')
          rows.splice(index, 1)
        }).catch(err => {
          console.log(err)
          that.$message.error('删除失败')
        })
      }).catch(() => {
        this.$message.success('取消成功')
      })
    }
  }
}
</script>

<style scoped>
.my-table-display {
  margin: 0 auto;
  padding: 20px;
  width: 90%;
  margin-top: 20px;
  display: flex;
}
.my-table-display .el-col {
  height: 60px;
}
.cell {
  height: 20px;
}
.my-flex {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.my-flex > div {
  padding-left: 15px;
}
</style>
