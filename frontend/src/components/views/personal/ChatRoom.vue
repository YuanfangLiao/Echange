<template>
  <div class="page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>个人中心</el-breadcrumb-item>
      <el-breadcrumb-item>消息中心</el-breadcrumb-item>
      <el-breadcrumb-item>聊天室</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="chat-content">
      <div class="chat-inner-top">
        <hr />
        与 {{ chatInfo.toUsername }} 的会话
        <hr />
      </div>
      <div class="chat-inner-center"
           id='chat-inner-center'>
        <div class="main-msg-box"
             v-for="(item,index) in chatMsg"
             :key="index">
          <img :src="baseUrl+item.img"
               width="50px"
               height="50px"
               style="border-radius:50px" />
          <div class="main-msg-box-right">
            <div class="main-msg-box-right-top">{{ item.username }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              &nbsp;&nbsp;&nbsp;&nbsp;{{item.time}}
            </div>
            <div class="main-msg-box-msg">
              {{ item.msg }}
            </div>
          </div>
        </div>
      </div>
      <div class="chat-inner-bottom">
        <el-row class="my-bottom-row">
          <el-col :span="20">
            <div class="grid-content bg-purple">
              <el-input placeholder="请输入内容"
                        v-model="inputMsg"
                        @keyup.enter.native="sendMsg"
                        clearable>
              </el-input>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple-light">
              <el-button type="success"
                         @click="sendMsg">发送消息</el-button>
            </div>
          </el-col>
        </el-row>
        <br />
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      baseUrl: this.$store.state.base_url,
      inputMsg: '',
      chatId: this.$route.params.id,
      chatInfo: {
        toUsername: ''
      },
      chatMsg: [{ 'time': '2019.04.29 12:28:33', 'user_id': 3, 'img': 'img/timg.jpg', 'username': 'user', 'msg': '消息' }]
    }
  },
  components: {

  },
  created () {
  },
  mounted () {
    let that = this
    that.$axios.get('/chat_api/getlist', {
      params: {
        id: that.$route.params.id
      }
    }).then(res => {
      this.chatInfo.toUsername = res.data.username
    }).catch(err => {
      console.log(err)
    })
    this.updateMsgList()
    // 聊天框滑到最底下
    let container = this.$el.querySelector('#chat-inner-center')
    container.scrollTop = container.scrollHeight
    // 循环发请求更新数据
    this.updateMsgInterval = setInterval(this.updateMsgList, 5000)
  },
  destroyed () {
    // 组件销毁时 清除定时任务
    clearInterval(this.updateMsgInterval)
  },
  methods: {
    sendMsg () {
      let that = this
      let msg = this.inputMsg
      if (!msg) { this.$message.warning('不能发送空消息'); return false }
      that.$axios.put('/chat_api/msg', {
        'msg': this.inputMsg,
        'id': this.chatId
      }).then(res => {
        if (res.data.flag === 'success') {
          that.$message.success('成功发送')
          that.inputMsg = ''
          that.updateMsgList()
        } else {
          that.$message.error('发送失败')
        }
      }).catch(err => {
        console.log(err)
        that.$message.error('请求失败')
      })
    },
    updateMsgList () {
      let that = this
      that.$axios.get('/chat_api/msg', {
        params: {
          id: that.$route.params.id
        },
        // 屏蔽加载动画
        isLoading: false
      }).then(res => {
        // console.log('res' + res.data.msg)
        that.chatMsg = res.data.msg
        // 聊天框滑到最底下
        let container = that.$el.querySelector('#chat-inner-center')
        container.scrollTop = container.scrollHeight
      })
    }
  }
}
</script>

<style scoped>
.chat-content {
  width: 90%;
  margin: 0 auto;
  margin-top: 30px;
  height: 650px;
  background-color: white;
  border-bottom: 1px solid #333;
}
.chat-inner-top {
  height: 50px;
}
.chat-inner-center {
  height: 540px;
  overflow: auto;
}
.chat-inner-bottom {
  height: 50px;
  padding-left: 10px;
  padding-top: 12px;
  border-top: 1px solid #333;
}
.my-bottom-row {
  height: 50px;
  margin: 0;
  padding: 0;
  margin-bottom: 10px;
}
.my-bottom-row .el-col {
  margin: 0;
  padding: 0;
}
.main-msg-box {
  text-align: left;
  padding: 10px;
  margin: 0 auto;
  width: 90%;
  display: flex;
  flex-direction: row;
}
.main-msg-box-right {
  padding-left: 20px;
}
.main-msg-box-msg {
  background-color: rgba(153, 169, 191, 0.3);
  border-radius: 5px;
  padding: 10px;
  font-size: 14px;
}
.main-msg-box-right-top {
  color: #909399;
  font-size: 12px;
  margin-bottom: 3px
}
</style>
