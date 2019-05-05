<template>
  <div>
    <el-carousel indicator-position="outside">
      <el-carousel-item v-for="(item,index) in carousels"
                        :key="index">
        <img :src="base_url1 + item.img"
             width="100%"
             height="100%">
      </el-carousel-item>
    </el-carousel>
    <br /><br />
    <!-- <el-row class="goods-row"> -->
    <div class="my-index-box">
      <el-col :span="8"
              v-for="item of goods_list"
              :key="item.id"
              :offset="item.id > 0 ? 2 : 0"
              class="goods-card">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="base_url + item.picture[0]"
               @click="dumpDetail(item.id)"
               class="image">
          <div style="padding: 14px;">
            <span>{{item.title}}</span>
            <div class="bottom clearfix">
              <time class="time">{{ item.create_time | date }}</time>
              <br /><br />
              <el-button type="text"
                         class="button"
                         @click="dumpDetail(item.id)">查看详情</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <!-- </el-row> -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      currentDate: new Date(),
      goods_list: [],
      base_url: this.$store.state.base_url,
      base_url1: this.$store.state.base_url1,
      carousels: []
    }
  },
  name: 'home',
  mounted: function () {
    let that = this
    console.log('hello')
    that.$axios.get('/goods/goods', {
      params: {
        query: 'index'
      }
    }).then(data => {
      that.goods_list = data.data
      console.log(that.base_url + that.goods_list[0].picture)
    })
    that.$axios.get('/api/carousel').then(res => {
      that.carousels = res.data
    })
  },
  filters: {
    date (time) {
      let date = new Date(time)// 把定义的时间赋值进来进行下面的转换
      let year = date.getFullYear()
      let month = date.getMonth() + 1
      let day = date.getDate()
      let hour = date.getHours()
      let minute = date.getMinutes()
      let second = date.getSeconds()
      return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
    }
  },
  methods: {
    dumpDetail (id) {
      this.$router.push(`/goods/${id}`)
    }
  }
}
</script>

<style scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}
.image:hover {
  cursor: pointer;
  opacity: 0.5;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
.goods-card {
  width: 200px;
  margin-left: 30px;
  padding-left: 0px;
  margin-top: 20px;
}
.goods-row {
  height: 300px;
}
.image {
  width: 200px;
  height: 200px;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.my-index-box {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  align-content: flex-start
}
</style>
