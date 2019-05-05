<template>
  <div class="page">
    <router-view name="personalDetail"></router-view>
    <div v-if="this.$route.name==='personalOrder'">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>个人中心</el-breadcrumb-item>
        <el-breadcrumb-item>换物中心</el-breadcrumb-item>
        <el-breadcrumb-item>我的换物</el-breadcrumb-item>
      </el-breadcrumb>
      <div class="my-table-display">
        <el-table :data="tableData"
                  stripe
                  :show-header="true"
                  style="width: 100%">

          <el-table-column prop="goods.title"
                           label="商品内容"
                           width="250">
            <template slot-scope="scope">
              <div class="my-flex">
                <img :src="base_url + scope.row.goods.picture[0]"
                     alt=""
                     style="width: 50px;height: 50px">
                <div>{{ scope.row.goods.title }}</div>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="msg"
                           width="120"
                           label="备注信息">
          </el-table-column>
          <el-table-column prop="status"
                           width="120"
                           label="订单状态">
            <template slot-scope="scope">
              <span style="color:red">{{ scope.row.status }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="create_time"
                           label="申请日期"
                           width="150">
            <template slot-scope="scope">
              {{ scope.row.create_time | timeFormat }}
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-tooltip class="item"
                          effect="dark"
                          content="点击查看商品详情"
                          placement="top">
                <el-button type="primary"
                           @click="goGood(scope.row.goods.id)"
                           icon="el-icon-search"
                           circle></el-button>
              </el-tooltip>
              <el-tooltip class="item"
                          effect="dark"
                          content="点击管理申请"
                          placement="top">
                <el-button type="warning"
                           @click="goEdit(scope.row.id)"
                           icon="el-icon-edit"
                           circle></el-button>
              </el-tooltip>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [],
      base_url: this.$store.state.base_url
    }
  },
  created () {
    this.$axios.get('/goods_api/order', {
      params: {
        query: 'mine'
      }
    }).then(res => {
      this.tableData = res.data
    })
  },
  methods: {
    goGood (id) {
      this.$router.push(`/goods/${id}`)
    },
    goEdit (id) {
      this.$router.push(`/personal/order/${id}`)
    }
  },
  components: {

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
.my-flex {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.my-flex > div {
  padding-left: 15px;
}
</style>
