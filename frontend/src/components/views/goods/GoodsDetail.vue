<template>
  <div class="page">
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
                     plain>我想要</el-button>
          <el-button type="warning">收藏</el-button>
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
          <img width="150px"
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
                       name="second"></el-tab-pane>

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
      similar_goods: {}
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
  width: auto;
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
</style>
