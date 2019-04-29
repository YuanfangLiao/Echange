<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>换物中心</el-breadcrumb-item>
      <el-breadcrumb-item>我的换物</el-breadcrumb-item>
      <el-breadcrumb-item>详情</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="inner-page">
      <hr style="background-color:#d3dce6;height:1px;border:none" />
      &nbsp;&nbsp;&nbsp;&nbsp;
      卖家：{{goodsDetail.publisher.username}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      预计交易地点：{{goodsDetail.publisher.address}}
      <div class="inner-info">
        <el-row style="height:100%">
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <img :src="getImgBaseUrl + goodsDetail.picture[0]"
                   width="130px">
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple-light">
              品名：{{goodsDetail.title}}<br />
              品牌：{{goodsDetail.brand}}<br />
              成色：{{goodsDetail.condition}}<br />
              预计交易地点：{{goodsDetail.publisher.address}}
            </div>
          </el-col>
          <el-col :span="12">
            <div class="grid-content price bg-purple">
              预估单价：<span style="color:#F56C6C">¥<span style="color:#F56C6C;font-size:20px">{{ goodsDetail.price }}</span></span>
            </div>
          </el-col>
        </el-row>
        <div class="grid-content msg bg-purple-light">
              给卖家留言:<br />
              <el-input type="textarea"
                        :rows="2"
                        placeholder="选填"
                        v-model="form.msg">
              </el-input>
            </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // 防止报错
      goodsDetail: {
        brand: 'python',
        condition: 99,
        create_time: '2019-04-18T21:04:27.302906+08:00',
        detail: '知识是无价的',
        id: 1,
        picture: ['img/timg.jpg'],
        price: 1000000,
        publisher: { id: 3, username: 'gople', email: 'lyf9708@163.com' },
        title: 'python知识',
        type: '其他',
        want: 'asdfsad'
      },
      form: {
        msg: '',
        goods_id: 0
      }
    }
  },
  created () {
    this.form.good_id = this.$route.params.id
    this.$axios.get('/goods_api/goods', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      this.goodsDetail = res.data[0]
      console.log(this.goodsDetail)
    }).catch(err => {
      console.log(err)
    })
    this.$axios.get('/goods/order', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      console.log(res.data[0])
      this.form.msg = res.data[0].msg
    })
  },
  mounted () {
  },
  components: {

  },
  computed: {
    getImgBaseUrl: function () {
      return this.$store.state.base_url
    }
  }
}
</script>

<style scoped>
.inner-page {
  width: 80%;
  margin: 0 auto;
  margin-top: 50px
}
.inner-info {
  background-color: RGBA(211, 220, 230, 0.3);
  padding: 20px;
  font-size: 12px;
  margin: 15px;
}
.grid-content {
  min-height: 50px;
  padding: 10px;
}
.price {
  line-height: 100px;
}
.msg {
  padding-top: 0px;
}
</style>
