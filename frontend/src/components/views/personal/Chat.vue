<template>
  <div class="page">
    <router-view name="personalDetail"></router-view>
    <div v-if="this.$route.name==='personalChat'">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>个人中心</el-breadcrumb-item>
        <el-breadcrumb-item>消息中心</el-breadcrumb-item>
      </el-breadcrumb>
      <div class="my-table-display">
        <el-table :data="tableData"
                  stripe
                  :show-header="true"
                  style="width: 100%">

          <el-table-column label="聊天对象"
                           width="500">
            <template slot-scope="scope">
              <div class="my-flex">
                <img :src="baseUrl + toUser(scope.row).picture"
                     alt=""
                     style="width: 50px;height: 50px">
                <div>{{ toUser(scope.row).username }}</div>
              </div>
            </template>
          </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-tooltip class="item"
                          effect="dark"
                          content="点击进入聊天界面"
                          placement="top">
                <el-button type="primary"
                          @click="goChat(scope.row.id)"
                           icon="el-icon-message"
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
      baseUrl: this.$store.state.base_url
      // username: localStorage.getItem('username')
      // to_username: ''
    }
  },
  computed: {

  },
  methods: {
    toUser: function (chatObj) {
      console.log(chatObj)
      // console.log(row)
      // let chatObj = row.tableData
      let user1 = chatObj.user1
      let user2 = chatObj.user2
      console.log(user1, user2)
      let myusername = localStorage.getItem('username')
      // 返回和登录用户聊天的username
      if (myusername === user1.username) return user2
      else return user1
    },
    goChat (id) {
      this.$router.push(`/personal/chat/${id}`)
    }
  },
  mounted () {
    let that = this
    that.$axios.get('/chat_api/getlist').then(res => {
      console.log(res.data)
      this.tableData = res.data
    })
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
