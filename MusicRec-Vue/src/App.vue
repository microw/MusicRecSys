<template>
  <div id="app">
    <router-view/>
    <new-footer />
  </div>
</template>

<script>
import newFooter from './components/newFooter'
export default {
  name: 'App',
  components: {
    'new-footer': newFooter
  },
  mounted () {
    if (localStorage.getItem('newslogintime')) {
      this.deTime(localStorage.getItem('newslogintime'), new Date(), 24)
    }
  }
}
</script>

<style lang="less">
  #app{
    overflow: auto;
  }
  /*改变vue-layer弹层样式*/
  .vl-notify-mask{
    opacity: 0.7;
  }
</style>
