<template>
  <div>
    <div class="goods-index-box"
         v-if="this.$route.name==='goods'">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>全部商品</el-breadcrumb-item>
      </el-breadcrumb>
      <br />
      <el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                @row-click="handleRowClick"
                @filter-change="filterChange"
                style="width: 100%">
        <el-table-column prop="id"
                         width="50">
        </el-table-column>
        <el-table-column prop="type"
                         column-key="type"
                         label="筛选种类"
                         :filters="typeFilter"
                         :filter-method="filterHandler"
                         width="120">
          <!--插入图片链接的代码-->
          <template slot-scope="scope">
            <img :src="base_url + scope.row.picture[0]"
                 alt=""
                 style="width: 80px;height: 80px">
          </template>
        </el-table-column>
        <el-table-column prop="title"
                         width="120">
          <template slot-scope="scope">
            品名: {{ scope.row.title }}<br />
            卖家: {{ scope.row.publisher.username }}
          </template>
        </el-table-column>
        <el-table-column prop="create_time"
                         width="180">
          <template slot-scope="scope">
            {{ scope.row.create_time | timeFormat }}<br />
            <!-- 卖家: {{ scope.row.publisher.username }} -->
          </template>
        </el-table-column>
        <el-table-column prop="want">
          <template slot-scope="scope">
            估价：<span style="color:#F56C6C">¥<span style="color:#F56C6C;font-size:20px">{{ scope.row.price }}</span></span><br />
            想换: {{ scope.row.want }}
          </template>
        </el-table-column>
        <el-table-column prop="publisher.address">
          <template slot-scope="scope">
            卖家位置：<br />
            {{ scope.row.publisher.address }}
          </template>
        </el-table-column>
      </el-table>
      <div class="my-pagination">
        <br />
        <el-pagination @size-change="handleSizeChange"
                       @current-change="handleCurrentChange"
                       :current-page.sync="currentPage"
                       :page-size="pagesize"
                       layout="prev, pager, next, jumper"
                       :total="total">
        </el-pagination>
      </div>
    </div>
    <keep-alive>
      <router-view :key="$route.fullPath"></router-view>
    </keep-alive>
  </div>
</template>

<script>
import { timeFormat } from '../../assets/js/filters.js'
export default {
  name: 'goods',
  data () {
    return {
      tableData: [],
      base_url: this.$store.state.base_url,
      // total: this.tableData.length, // 默认数据总数
      pagesize: 5, // 每页的数据条数
      currentPage: 1, // 默认开始页面
      typeFilter: [],
      typeObject: {},
      total: 0
    }
  },
  created () {
    let that = this
    that.$axios.get('/api/all_goods_type').then(res => {
      let temp = res.data.data
      let result = []
      for (let item of temp) {
        result.push({
          'value': item.value,
          'text': item.label
        })
        this.typeObject[item.value] = item.label
      }
      that.typeFilter = result
      // console.log(res.data.data)
    })
  },
  methods: {
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage
    },
    handleSizeChange: function (val) {
      this.pageSize = val
      this.currentPage = 1
      // this.fetchData(1, val)
    },
    handleRowClick: function (row, column, event) {
      console.log(row)
      this.$router.push(`/goods/${row.id}`)
    },
    filterHandler (value, row, column) {
      // const property = column['property']
      console.log(value)
      return row.type === this.typeObject[value]
    },
    filterChange (filters) {
      if (filters.type) {

      }
    }
  },
  computed: {

  },
  filters: {
    timeFormat
  },
  mounted () {
    this.$axios.get('/goods_api/goods').then(res => {
      this.tableData = res.data
      this.total = res.data.length
      // console.log(this.tableData)
    })
  },

  components: {

  }
}
</script>

<style scoped>
.goods-index-box {
  margin: 0 auto;
  width: 80%;
}
.my-pagination {
  width: 100%;
  margin: 0 auto;
  text-align: center;
}
</style>
