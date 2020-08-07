<template>
  <div class="post-container">
    <h2>{{ title }}</h2>
    <div class="sender-info">
      <span class="sender">{{ sender }}</span>
      <span class="date">{{ date.split(' ')[0] }}</span>
    </div>
    <div>
      <p class="desc">{{ desc.slice(0, 120) }}</p>
    </div>
    <el-button class="visit" @click="visit" type="text">查看</el-button>
  </div>
</template>

<script>
export default {
  name: 'post-container',
  props: {
    id: String,
    title: String,
    desc: String,
    date: String,
    sender: String,
  },
  methods: {
    visit() {
      this.$router.push({ name: 'PostDetail', params: { id: this.id } })
    },
  },
}
</script>

<style lang="scss" scoped>
.post-container {
  margin: 30px 10%;
  margin-bottom: 0;
  padding: 25px 35px;
  position: relative;
  width: 80%;
  height: 200px;
  background-color: rgb(240, 240, 240);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
  border-radius: 1px;
}
h2 {
  margin: 0;
  padding: 0;
  font-size: 1.25em;
  font-weight: 600;
}
.sender-info {
  font-size: 1em;
  margin-top: 8px;
  margin-bottom: 10px;
  .sender {
    font-weight: 500;
    margin-right: 20px;
  }
  .date {
    color: grey;
  }
}
.visit {
  position: absolute;
  bottom: 15px;
}
</style>
