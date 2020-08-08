<template>
  <div class="comment-container">
    <div class="sender-info">
      <span class="sender">{{ sender }}</span>
      <span class="date">{{ date.split(' ')[0] }}</span>
    </div>
    <div>
      <p class="content">{{ content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'comment-container',
  props: {
    content: String,
    date: String,
    sender: String,
  },
}
</script>

<style lang="scss" scoped>
.comment-container {
  margin: 30px 0;
  margin-bottom: 0;
  padding: 25px 35px;
  position: relative;
  height: 150px;
  background-color: rgb(240, 240, 240);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
  border-radius: 1px;
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
</style>
