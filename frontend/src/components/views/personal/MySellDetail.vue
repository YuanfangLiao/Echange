<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>换物中心</el-breadcrumb-item>
      <el-breadcrumb-item>物主中心</el-breadcrumb-item>
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
        <!-- <hr style="background-color:#d3dce6;height:1px;border:none" /> -->
        交易状态 :<span style="color:red">{{ form.status }} </span>
        &nbsp; &nbsp; &nbsp; &nbsp;
        交易创建时间 :<span >{{ form.create_time | timeFormat }} </span>
        <hr style="background-color:#d3dce6;height:1px;border:none" />
        <div class="grid-content msg bg-purple-light">
          买家的留言:<br />
          <el-input type="textarea"
                    :rows="2"
                    disabled=""
                    placeholder="选填"
                    v-model="form.msg">
          </el-input>
        </div>
      </div>
    </div>
    <div class="my-operation-field">
      <el-button type="success"
                 @click="contactBuyer"
                 round>联系买家</el-button>
      <el-tooltip class="item"
                  effect="dark"
                  content="当卖家确认交易后买家方可确认收货"
                  placement="top">
        <el-button type="success"
                   :disabled="getConfirmButtonStatus"
                   @click="confirmOrder"
                   round>确认交易</el-button>
      </el-tooltip>
      <el-tooltip class="item"
                  effect="dark"
                  content="拒绝交易"
                  placement="top">
        <el-button type="danger"
                   :disabled="getConfirmButtonStatus"
                   @click="cancelOrder"
                   round>取消交易</el-button>
      </el-tooltip>
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
        goods_id: 0,
        buyer_id: 0,
        id: '',
        create_time: ''
      },
      getConfirmButtonStatus: true
    }
  },
  created () {
    this.form.good_id = this.$route.params.id
    this.$axios.get('/goods_api/goods', {
      params: {
        order_id: this.$route.params.id
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
      this.form.buyer_id = res.data[0].buyer
      this.form.id = res.data[0].id
      this.form.status = res.data[0].status
      this.form.create_time = res.data[0].create_time
      if (res.data[0].status === '待沟通') {
        this.getConfirmButtonStatus = false
      }
    })
  },
  computed: {
    getImgBaseUrl: function () {
      return this.$store.state.base_url
    }
  },
  methods: {
    contactBuyer: function () {
      let that = this
      that.$axios.post('/chat_api/msg', {
        to_user_id: that.form.buyer_id
      }).then(res => {
        let flag = res.data.flag
        if (flag === 'success') {
          let chatId = res.data.chat_id
          this.$router.push(`/personal/chat/${chatId}`)
        } else {
          this.$message.error(res.data.msg)
        }
      }).catch(err => {
        console.log(err)
      })
    },
    confirmOrder: function () {
      this.$confirm('确定无误接收交易吗？确认交易意味着您已和买家谈妥，达成交易意向', '交易确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.$axios.put('/goods_api/order', {
          id: that.form.id,
          status: 2
        }).then(res => {
          let flag = res.data.flag
          if (flag === 'success') {
            that.getConfirmButtonStatus = true
            this.$message.success('已确认交易')
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消确认收货'
        })
      })
    },
    cancelOrder: function () {
      this.$confirm('确定取消交易吗？取消交易意味着您拒绝该交易请求', '交易确认', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.$axios.put('/goods_api/order', {
          id: that.form.id,
          status: 3
        }).then(res => {
          let flag = res.data.flag
          if (flag === 'success') {
            that.getConfirmButtonStatus = true
            this.$message.warning('已取消交易')
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消'
        })
      })
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
