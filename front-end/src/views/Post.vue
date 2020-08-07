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
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'

export default {
  name: 'Post',
  mixins: [checkUsrMixin],
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    }
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
          if (obj.checkUsr(response)) {
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
#post {
  padding: 20px 50px;

  .edit-area {
    background-color: rgb(245, 245, 245);
    height: 350px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
    border-radius: 2px;
    padding: 30px 40px;
  }
}
</style>
