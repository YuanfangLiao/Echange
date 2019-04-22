<template>
  <div>
    <div v-if="this.$route.name==='goods'">这是父组件</div>
    <keep-alive>
      <router-view :key="$route.fullPath"></router-view>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: 'goods',
  data () {
    return {

    }
  },
  methods: {

  },
  computed: {

  },
  mounted () {

  },
  components: {

  }
}
</script>

<style scoped>
</style>
