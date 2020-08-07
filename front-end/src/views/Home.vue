<template>
  <div id="home">
    <PostContainer
      v-for="item in posts"
      :key="item.id"
      :id="item.id"
      :title="item.title"
      :sender="item.sender"
      :date="item.date"
      :desc="item.content"
    />
  </div>
</template>

<script>
import PostContainer from '@/components/PostContainer.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    PostContainer,
  },
  data() {
    return {
      posts: [],
    }
  },
  mounted() {
    let obj = this

    axios
      .get(this.$hostname + 'post/all')
      .then(function(response) {
        obj.posts = response.data
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })
  },
}
</script>

<style lang="scss" scoped>
#home {
  height: 100%;
  width: 100%;
  overflow: auto;
}
</style>
