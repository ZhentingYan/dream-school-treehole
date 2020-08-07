<template>
  <div id="post-detail">
    <div class="sender-info">
      <span class="sender">{{ sender }}</span>
      <span class="date">{{ date.split(' ')[0] }}</span>
    </div>
    <h2>{{ title }}</h2>
    <div>
      <p class="content">{{ content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'post-detail',
  data() {
    return {
      sender: '',
      date: '',
      title: '',
      content: '',
    }
  },
  mounted() {
    let obj = this

    axios
      .get(this.$hostname + 'post/info', {
        params: {
          id: obj.$route.params.id,
        },
      })
      .then(function(response) {
        console.log(response.data)
        obj.sender = response.data.sender
        obj.date = response.data.date
        obj.title = response.data.title
        obj.content = response.data.content
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })
  },
}
</script>

<style lang="scss" scoped>
#post-detail {
  margin: 50px 10%;
  padding: 30px 30px;
  width: 80%;
  background-color: rgb(250, 250, 250);
}
.sender-info {
  font-size: 1em;
  margin-bottom: 10px;
  .sender {
    font-weight: 500;
    margin-right: 15px;
  }
  .date {
    color: grey;
  }
}
h2 {
  margin: 10px 0;
  padding: 0;
  font-size: 1.25em;
  font-weight: 600;
}
.content {
  margin-top: 30px;
}
</style>
