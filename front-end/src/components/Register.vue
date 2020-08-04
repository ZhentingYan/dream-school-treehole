<template>
  <div id="register">
    <el-form
      ref="form"
      status-icon
      :model="form"
      :rules="rule"
      label-width="80px"
    >
      <el-form-item label="用户昵称" prop="usr">
        <el-input
          v-model="form.usr"
          autocomplete="off"
          placeholder="输入您的昵称"
        />
      </el-form-item>
      <el-form-item label="输入密码" prop="pwd">
        <el-input
          type="password"
          v-model="form.pwd"
          autocomplete="off"
          placeholder="输入您的密码"
        />
      </el-form-item>
      <el-form-item label="确认密码" prop="pwd2">
        <el-input
          type="password"
          v-model="form.pwd2"
          autocomplete="off"
          placeholder="验证您的密码"
        />
      </el-form-item>
      <el-form-item label="真实姓名" prop="name">
        <el-input
          v-model="form.name"
          autocomplete="off"
          placeholder="输入真实姓名"
        />
      </el-form-item>
      <el-form-item label="学号" prop="number">
        <el-input
          v-model="form.number"
          autocomplete="off"
          placeholder="（学生无需填写）"
        />
      </el-form-item>
      <el-form-item label="选择身份">
        <el-select v-model="form.role" placeholder="学生/志愿者">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item class="btn">
        <el-button type="primary" @click="SignUp">注册</el-button>
        <el-button @click="$emit('change')">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请确认您的密码'))
      } else if (value !== this.form.pwd) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    var validate = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('内容不得为空'))
      } else {
        callback()
      }
    }
    return {
      form: {
        usr: '',
        pwd: '',
        pwd2: '',
        name: '',
        role: '',
        number: '',
      },
      rule: {
        pwd2: [{ validator: validatePass, trigger: 'blur' }],
        pwd: [{ validator: validate, trigger: 'blur' }],
        usr: [{ validator: validate, trigger: 'blur' }],
        name: [{ validator: validate, trigger: 'blur' }],
      },
      options: [
        { value: 'student', label: '学生' },
        { value: 'volunteer', label: '志愿者' },
      ],
    }
  },
  methods: {
    SignUp: function() {
      if (
        this.form.pwd == this.form.pwd2 &&
        this.form.pwd != '' &&
        this.form.usr != '' &&
        this.form.role != '' &&
        this.form.name != ''
      ) {
        let obj = this
        var params = new URLSearchParams()
        params.append('usr', obj.form.usr)
        params.append('pwd', obj.form.pwd)
        params.append('name', obj.form.name)
        params.append('role', obj.form.role)
        params.append('number', obj.form.number)

        axios({
          method: 'post',
          url: this.$hostname + 'auth/register',
          data: params,
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        })
          .then(function(response) {
            console.log(response)
            if (response.data == 'True') {
              obj.$message({ message: '注册成功！', type: 'success' })
              obj.$emit('change')
            } else if (response.data == 'Taken') {
              obj.$message({ message: '用户名已占用', type: 'warning' })
              obj.form.usr = ''
            }
          })
          .catch(function() {
            obj.$message.error('糟糕，哪里出了点问题！')
          })
      } else {
        this.$message.error('请确认输入内容全部正确！')
      }
    },
  },
}
</script>

<style scoped>
#register {
  float: right;
  margin-top: 60px;
  margin-right: 100px;
  width: 450px;
}
.btn {
  margin-top: 20px;
  margin-right: 10px;
}
</style>
