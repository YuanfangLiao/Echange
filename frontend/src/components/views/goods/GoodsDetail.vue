<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>全部商品</el-breadcrumb-item>
      <el-breadcrumb-item>详细信息</el-breadcrumb-item>
    </el-breadcrumb>
    <br />
    <el-row>
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <div class="block">
            <el-carousel trigger="click"
                         indicator-position="outside">
              <el-carousel-item v-for="item in good_detail.picture"
                                :key="item"
                                class="img-father">
                <img :src="getImgBaseUrl + item"
                     width="100%">
              </el-carousel-item>
            </el-carousel>
          </div>
        </div>
      </el-col>
      <el-col :span="10">
        <div class="grid-content bg-purple-light content-top-middle">
          <h4>&nbsp;&nbsp;{{ good_detail.title }}</h4>
          <el-alert type="error"
                    :closable="false">
            预估换物价：¥ <span style="font-size:28px">{{ good_detail.price }}</span>
          </el-alert>
          <el-alert type="info"
                    :closable="false">
            卖家想换：{{ good_detail.want }}
          </el-alert>
          <p class="small-text">商品编号: &nbsp;&nbsp;&nbsp;&nbsp;
            {{ good_detail.id }}
          </p>
          <p class="small-text">品&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;牌:
            &nbsp;&nbsp;&nbsp;&nbsp;
            {{ good_detail.brand }}
          </p>
          <p class="small-text">成&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;色:
            &nbsp;&nbsp;&nbsp;&nbsp;
            {{ good_detail.condition }}成新
          </p>
          <p class="small-text">类&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;型:
            &nbsp;&nbsp;&nbsp;&nbsp;
            {{ good_detail.type }}
          </p>
          <hr />
          <p class="small-text">发布时间:
            &nbsp;&nbsp;&nbsp;&nbsp;
            {{ good_detail.create_time | timeFormat }}
          </p>
          <el-button type="primary"
                     @click="goWant"
                     v-if="!isOrdered && good_detail.active"
                     plain>我想要</el-button>
          <el-button type="primary"
                     v-if="isOrdered && good_detail.active"
                     disabled=""
                     plain>您已申请</el-button>
          <el-button type="warning"
                     v-if="!isCollected && good_detail.active"
                     @click="goCollection">
            收藏</el-button>
          <el-button type="warning"
                     v-if="isCollected && good_detail.active"
                     @click="goCollection">
            取消收藏</el-button>
          <el-button type="warning"
                     disabled
                     v-if="!good_detail.active">
            该商品已经卖出或下架，仅供查看</el-button>
        </div>
      </el-col>
      <el-col :span="6"
              v-if="good_detail.publisher">
        <div class="grid-content bg-purple">
          <div class="content-top-right">
            <img src="../../../../static/img/maijiaxinxi.png"
                 width="100%" />
            <hr style="background-color:#d3dce6;height:1px;border:none" />
            <div class="inner-info">
              <el-row style="height:60px">
                <el-col :span="6"><img :src="getImgBaseUrl + good_detail.publisher.picture"
                       width="60px"
                       height="60px"
                       style="border-radius:100px" /></el-col>
                <el-col :span="18"
                        style="padding-left:10px">
                  <p class="small-text">个人签名：
                  </p>
                  <p class="small-text">{{ good_detail.publisher.signature }}
                  </p>
                </el-col>
              </el-row>

              <p class="small-text">卖家&nbsp;&nbsp;&nbsp;&nbsp;id:
                &nbsp;&nbsp;&nbsp;&nbsp;
                {{ good_detail.publisher.id }}
              </p>
              <p class="small-text">卖家昵称:
                &nbsp;&nbsp;&nbsp;&nbsp;
                {{ good_detail.publisher.username }}
              </p>
              <p class="small-text">卖家等级:
                &nbsp;&nbsp;&nbsp;&nbsp;
                level.{{ good_detail.publisher.level }}
              </p>
              <p class="small-text">卖家信用:
                &nbsp;&nbsp;&nbsp;&nbsp;
                {{ good_detail.publisher.credit }}分
              </p>
              <p class="small-text">卖家地址:
                &nbsp;&nbsp;&nbsp;&nbsp;
                {{ good_detail.publisher.address }}
              </p>
              <div style="padding-left:70px">
                <el-tooltip class="item"
                            effect="dark"
                            content="给卖家发邮件告诉他你的意向"
                            placement="top">
                  <el-button type="info"
                             icon="el-icon-message"
                             size="mini"
                             circle></el-button>
                </el-tooltip>
                <el-tooltip class="item"
                            effect="dark"
                            content="和卖家在系统中沟通"
                            placement="top">
                  <el-button type="info"
                             icon="el-icon-mobile-phone"
                             @click="goChat"
                             size="mini"
                             circle></el-button>
                </el-tooltip>
              </div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
    <p>&nbsp;</p>
    <hr style="background-color:#d3dce6;height:1px;border:none" />
    <el-container>
      <el-aside width="250px"
                style="padding-top:8px">为你推荐
        <hr style="background-color:#d3dce6;height:1px;border:none" />
        <div v-for="item of similar_goods "
             :key="item.id"
             style="border-bottom:1px dashed #d3dce6;margin-bottom:10px">
          <img width="150px" height="150px"
               @click="goAnother(item.id)"
               :src="getImgBaseUrl+item.picture[0]" />
          <br />
          <a @click="goAnother(item.id)">{{ item.title }}</a>
          <br />
        </div>
      </el-aside>
      <el-main>
        <el-tabs v-model="activeName"
                 type="card"
                 @tab-click="handleClick">
          <el-tab-pane label="产品介绍"
                       name="first">
            <div class="inner-detail-good">
              <p style="border-bottom:1px dashed #d3dce6;margin-bottom:10px">
                商品名称： {{ good_detail.title }} &nbsp;&nbsp;&nbsp;&nbsp;
                换物价： {{ good_detail.price }}.00(元) &nbsp;&nbsp;&nbsp;&nbsp;
                商品类型： {{ good_detail.type }}<br /><br /></p>
              <br />
              卖家介绍: &nbsp;&nbsp;&nbsp;&nbsp;{{ good_detail.detail }}
              <br /> <br />
              详细大图：
              <br /> <br />
              <div>

                <img v-for="item of good_detail.picture"
                     :key="item"
                     :src="getImgBaseUrl + item"
                     width="400px"
                     style="margin-bottom:10px" />

              </div>
            </div>
          </el-tab-pane>
          <el-tab-pane label="常见问题"
                       name="second">
            <div>
              <div class="inner-detail-detail">
                <p style="border-bottom:1px dashed #d3dce6;margin-bottom:10px">
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;免责声明：<br /><br />
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EChange易物网站所展示的商品供求信息由买卖双方自行提供，其真实性、准确性和合法性由信息发布人负责。EChange不提供任何保证，并不承担任何法律责任。<br /><br />
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EChange友情提醒：<br /><br />
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为保障您的利益，请现场成交，贵重物品，请妥善交易。<br /><br />
                </p>
                <div class="question_tp">什么是EChange</div>
                <div class="question_dw">
                  <p>答：EChange是校园物品交换网站，方便您随时随地的对于您的商品进行管理，支持您随时易货，给您提供方便、快捷、安全的易货交易。</p>
                </div>

                <div class="question_tp">我们网站是做什么的</div>
                <div class="question_dw">
                  <p>答：我们是一个以物易物的网站，提供易物平台，您可以在我们网站上注册会员账号并通过实名认证后，可以发布您的商品或服务，将您的商品或服务换取您需要的商品或服务。</p>
                </div>

                <div class="question_tp">关于发货</div>
                <div class="question_dw">
                  <p style="text-align: left;">EChange作为第三方交易平台，在线交易的每一笔订单都需要双方自行协商发货。我们提醒换客在交换商品前认真核实信息，如您对商品详情等任何信息有疑问，请在交易前与对方沟通确认。</p>
                </div>

                <div class="question_tp">开发票的事宜</div>
                <div class="question_dw">
                  <p>答：发票是由商家直接给您开具的，具体事宜您可以直接咨询商家。</p>
                </div>

                <div class="question_tp">建议交换商品类型</div>
                <div class="question_dw">
                  <p>答：我们建议您选择换什么的基本条件：第一是您需要的用的上的商品；第二是您周围人需要并且很好卖出去的商品；第三就是放着也能升值的商品。</p>
                </div>

                <div class="question_tp">可以无理由退换货吗</div>
                <div class="question_dw">
                  <p>答：请在易物以及购买前仔细查看商家的服务条款，目前商品的售后服务都由商家给您提供，每个商家都是不一样的。</p>
                </div>

                <div class="question_tp">发票的具体问题</div>
                <div class="question_dw">
                  <p>答：发票是由商家直接给您开具的，在发票信息栏中显示的信息就是可选用的，没有显示的，就不能填写或选择使用的哦。</p>
                </div>

                <div class="question_tp">关于售后服务</div>
                <div class="question_dw">
                  <p>答：目前商品的售后服务都由商家给您提供，如有疑问，可以随时拨打EChange客服中心电话178-6542-3119。</p>
                </div>

              </div>
            </div>
          </el-tab-pane>

        </el-tabs>

      </el-main>
    </el-container>
  </div>
</template>

<script>
import { timeFormat } from '../../../assets/js/filters.js'
export default {
  data () {
    return {
      good_id: '',
      good_detail: {},
      activeName: 'first',
      similar_goods: {},
      isCollected: false,
      isOrdered: false
    }
  },
  methods: {
    handleClick (tab, event) {
      console.log(tab, event)
    },
    goAnother (id) {
      this.$router.replace(`/goods/${id}`)
    },
    initData () {
      console.log('路由发送变化doing...')
    },
    goWant () {
      this.$router.push(`/goods/${this.$route.params.id}/want`)
    },
    goCollection () {
      let that = this
      let params = that.$qs.stringify({
        id: this.$route.params.id
      })
      console.log(this.$route.params.id)
      this.$axios.post('/goods_api/collection', params).then(res => {
        that.$message.success(res.data.msg)
        if (res.data.msg === '收藏成功') this.isCollected = true
        else this.isCollected = false
      }).catch(err => {
        console.log(err)
      })
    },
    goChat () {
      let that = this
      that.$axios.post('/chat_api/msg', {
        to_user_id: that.good_detail.publisher.id
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
    }
  },
  watch: {
    '$route': 'initData'
  },
  filters: {
    timeFormat
  },
  created () {
    var self = this
    self.initData()
    this.$axios.get('/api/similar_goods', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      this.similar_goods = res.data
    })
    // 检查是否收藏
    this.$axios.get('/goods_api/collection', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      console.log(res.data)
      this.isCollected = res.data.msg
    })
    // 检查是否购买
    this.$axios.get('/api/user_goods_check', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      if (res.data.flag === 'fail') { this.isOrdered = true }
    })
  },
  mounted () {
    window.scroll(0, 0)
    this.good_id = this.$route.params.id
    this.$axios.get('/goods_api/goods', {
      params: {
        id: this.$route.params.id
      }
    }).then(res => {
      this.good_detail = res.data[0]
    }).catch(err => {
      console.log(err)
    })
  },
  computed: {
    getImgBaseUrl: function () {
      return this.$store.state.base_url
    }
  },
  components: {

  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.block {
  width: 350px;
  height: 350px;
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  /* border: 1px solid #d3dce6; */
  border-radius: 10px;
  background-color: RGBA(211, 220, 230, 0.3);
}
.block img {
  position: relative;
  max-height: 100%;
  max-width: 100%;
  width: 100%;
  height: auto;
  top: 50%;
  left: 50%;
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

.el-row {
  margin-bottom: 20px;
  /* &:last-child {
      margin-bottom: 0;
    } */
}
.grid-content {
  color: #909399;
  /* padding-top: -10px */
}
.small-text {
  font-size: 12px;
}
.content-top-middle {
  margin-top: -15px;
}
.content-top-right {
  margin-left: 20px;
  min-height: 350px;
  border: 1px solid #d3dce6;
  /* background-color:  #909399; */
}
.inner-info {
  padding-left: 20px;
}
.el-aside {
  /* background-color: #d3dce6; */
  border: 1px solid #d3dce6;
  color: #333;
  min-height: 600px;
  text-align: center;
  /* line-height: 200px; */
}

.el-main {
  /* background-color: #e9eef3; */
  color: #333;
  min-height: 600px;
  padding: 0;
  /* border-left: 1px solid #d3dce6; */
  border-right: 1px solid #d3dce6;
  border-bottom: 1px solid #d3dce6;
  /* text-align: center; */
  /* line-height: 160px; */
}
.inner-detail-good {
  padding: 20px;
}
.inner-detail-good p {
  font-size: 12px;
  display: block;
  margin-top: 0;
  padding-top: 0;
}
.inner-detail-good div {
  display: flex;
  flex-direction: column;
}
.el-icon-arrow-right {
  margin-bottom: 20px;
}
p {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
.inner-detail-deatail {
  padding: 20px;
}
.inner-detail-detail p {
  font-size: 12px;
  display: block;
  margin-top: 0;
  padding-top: 0;
}
.inner-detail-detail div {
  display: flex;
  flex-direction: column;
}
.question_tp {
  margin-top: 0;
  padding-top: 0;
  padding: 18px;
  font-size: 18px;
}
.question_dw {
  /* margin-top: 0;
  padding-top:0; */
  padding: 40px;
  font-size: 18px;
}
</style>
