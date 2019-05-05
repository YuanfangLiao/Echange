<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>全部商品</el-breadcrumb-item>
      <el-breadcrumb-item>交换确认</el-breadcrumb-item>
    </el-breadcrumb>
    <h3>交换意向确认页面</h3>
    <hr style="background-color:#d3dce6;height:1px;border:none" />
    &nbsp;&nbsp;&nbsp;&nbsp;
    卖家：{{goodsDetail.publisher.username}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    预计交易地点：{{goodsDetail.publisher.address}}
    <div class="inner-info">
      <el-row style="height:100%">
        <el-col :span="5">
          <div class="grid-content bg-purple">
            <img :src="getImgBaseUrl + goodsDetail.picture[0]"
                 width="130px">
          </div>
        </el-col>
        <el-col :span="5">
          <div class="grid-content bg-purple-light">
            品名：{{goodsDetail.title}}<br />
            品牌：{{goodsDetail.brand}}<br />
            成色：{{goodsDetail.condition}}<br />
            预计交易地点：{{goodsDetail.publisher.address}}
          </div>
        </el-col>
        <el-col :span="5">
          <div class="grid-content price bg-purple">
            预估单价：<span style="color:#F56C6C">¥<span style="color:#F56C6C;font-size:20px">{{ goodsDetail.price }}</span></span>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content msg bg-purple-light">
            给卖家留言:<br />
            <el-input type="textarea"
                      :rows="2"
                      placeholder="选填"
                      v-model="form.msg">
            </el-input>
          </div>
        </el-col>
      </el-row>
    </div>
    <hr style="background-color:#d3dce6;height:1px;border:none" />
    <el-button type="primary"
               @click="goWant"
               plain>确认无误，提交意向</el-button>
    <el-button type="warning"
               @click="goBack">我再想想</el-button>
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
    this.good_id = this.$route.params.id
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
  },
  mounted () {
    // 检查是否已经提交过意向
    this.$axios.get('/api/user_goods_check', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      // 发布成功
      if (res.data.flag !== 'success') {
        this.$notify.error({ title: '您已经提交过了',
          message: res.data.msg })
        this.$router.push('/home')
      }
    }).catch(err => {
      console.log(err)
    })
  },
  components: {

  },
  computed: {
    getImgBaseUrl: function () {
      return this.$store.state.base_url
    }
  },
  methods: {
    goWant () {
      this.$confirm('确定信息无误提交吗，亲？', '发布确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.form.goods_id = this.goodsDetail.id
        let that = this
        that.$axios.post('/goods_api/order', this.form).then(res => {
          // 发布成功
          if (res.data.flag === 'success') {
            this.$notify.success({ title: '申请成功',
              message: '申请交易意向成功' })
            this.$router.push('/personal/order')
          } else {
            this.$notify.error({ title: '申请失败',
              message: res.data.error })
          }
        }).catch(err => {
          this.$notify.error({ title: '发布失败',
            message: '发布申请失败' })
          console.log(err)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消发布'
        })
      })
    },
    goBack () {
      this.$router.back(-1)
    }
  }
}
</script>

<style scoped>
.page {
  width: 80%;
  margin: 0 auto;
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
  padding-top: 30px;
}
</style>
