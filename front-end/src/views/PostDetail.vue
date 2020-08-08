<template>
  <div id="post-detail">
    <div class="post-info">
      <div class="sender-info">
        <span class="sender">{{ sender }}</span>
        <span class="date">{{ date.split(' ')[0] }}</span>
      </div>
      <h2>{{ title }}</h2>
      <div>
        <p class="content">{{ content }}</p>
      </div>
    </div>
    <div class="comment">
      <el-form ref="form" :model="form">
        <el-form-item prop="comment">
          <el-input
            type="textarea"
            :autosize="{ minRows: 5 }"
            placeholder="请输入评论内容"
            v-model="form.comment"
          />
        </el-form-item>
        <el-form-item class="btn">
          <el-button type="primary" @click="Send">发布评论</el-button>
        </el-form-item>
      </el-form>
    </div>
    <CommentContainer
      v-for="item in comments"
      :key="item.id"
      :sender="item.sender"
      :date="item.date"
      :content="item.content"
    />
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'
import CommentContainer from '@/components/CommentContainer.vue'

export default {
  name: 'post-detail',
  mixins: [checkUsrMixin],
  data() {
    return {
      sender: '',
      date: '',
      title: '',
      content: '',
      form: {
        comment: '',
      },
      comments: [],
    }
  },
  components: {
    CommentContainer,
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
        obj.sender = response.data.sender
        obj.date = response.data.date
        obj.title = response.data.title
        obj.content = response.data.content
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })

    axios
      .get(this.$hostname + 'comment/all', {
        params: {
          id: obj.$route.params.id,
        },
      })
      .then(function(response) {
        obj.comments = response.data
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })
  },
  methods: {
    Send() {
      let obj = this
      let params = new URLSearchParams()
      params.append('post-id', obj.$route.params.id)
      params.append('content', obj.form.comment)

      axios({
        method: 'post',
        url: this.$hostname + 'comment/new',
        data: params,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      })
        .then(function(response) {
          if (obj.checkUsr(response.data)) {
            obj.$message({ message: '发布成功！', type: 'success' })
            obj.form.comment = ''
          }
        })
        .catch(function() {
          obj.$message.error('糟糕，哪里出了点问题！')
        })
    },
  },
}
</script>

<style lang="scss" scoped>
#post-detail {
  margin: 30px 10%;
  width: 80%;
}
.post-info {
  background-color: rgb(245, 245, 245);
  padding: 25px 35px;
  border-radius: 1px;
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
}
.comment {
  padding: 25px 35px;
  background-color: rgb(245, 245, 245);
}
</style>
