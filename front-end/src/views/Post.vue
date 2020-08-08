<template>
  <div id="post">
    <div class="edit-area">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="发布主题" prop="title">
          <el-input v-model="form.title" placeholder="主题" />
        </el-form-item>
        <el-form-item label="发布内容" prop="content">
          <el-input
            type="textarea"
            :autosize="{ minRows: 5 }"
            placeholder="请输入内容"
            v-model="form.content"
          />
        </el-form-item>
        <el-form-item class="btn">
          <el-button type="primary" @click="Send">发送</el-button>
        </el-form-item>
      </el-form>
    </div>
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
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'
import PostContainer from '@/components/PostContainer.vue'

export default {
  name: 'Post',
  mixins: [checkUsrMixin],
  components: {
    PostContainer,
  },
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
      posts: [],
    }
  },
  mounted() {
    let obj = this

    axios
      .get(this.$hostname + 'post/mine')
      .then(function(response) {
        if (obj.checkUsr(response.data)) {
          obj.posts = response.data
        }
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })
  },
  methods: {
    Send: function() {
      let obj = this
      let params = new URLSearchParams()
      params.append('title', obj.form.title)
      params.append('content', obj.form.content)

      axios({
        method: 'post',
        url: this.$hostname + 'post/new',
        data: params,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      })
        .then(function(response) {
          if (obj.checkUsr(response.data)) {
            obj.$message({ message: '发布成功！', type: 'success' })
            obj.form.title = ''
            obj.form.content = ''
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
.edit-area {
  margin: 30px 10%;
  margin-bottom: 0;
  padding: 30px;
  padding-top: 40px;
  background-color: rgb(240, 240, 240);
  height: 350px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
  border-radius: 1px;
}
</style>
