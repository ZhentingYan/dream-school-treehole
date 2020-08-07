<template>
  <div id="personinfo">
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
          :disabled="true"
        />
      </el-form-item>
      <el-form-item label="真实姓名" prop="name">
        <el-input
          v-model="form.name"
          autocomplete="off"
          placeholder="输入真实姓名"
          :disabled="true"
        />
      </el-form-item>
      <!-- <el-form-item label="重置密码" prop="pwd">
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
      </el-form-item> -->
      <el-form-item label="学号" prop="number">
        <el-input
          v-model="form.number"
          autocomplete="off"
          :disabled="true"
          placeholder="（学生无需填写）"
        />
      </el-form-item>
      <el-form-item label="会员身份" prop="number">
        <el-input
          v-model="form.role"
          :disabled="true"
          placeholder="（学生无需填写）"
        />
      </el-form-item>
      <el-form-item class="btn">
        <!-- <el-button type="primary" @click="Edit" plain>修改</el-button> -->
        <el-button type="warning" @click="LogOut" plain>退出登陆</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'

export default {
  name: 'person-info',
  mixins: [checkUsrMixin],
  data() {
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请确认您的密码'))
      } else if (value !== this.form.pwd) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    let validate = (rule, value, callback) => {
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
      options: { student: '学生', volunteer: '志愿者' },
    }
  },
  mounted() {
    let obj = this

    axios
      .get(this.$hostname + 'user/info')
      .then(function(response) {
        if (obj.checkUsr(response.data)) {
          obj.form.usr = response.data.usr
          obj.form.name = response.data.name
          obj.form.role = obj.options[response.data.role]
          obj.form.number = response.data.number
        }
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！')
      })
  },
  methods: {
    // Edit: function() {
    //   if (
    //     this.form.pwd == this.form.pwd2 &&
    //     this.form.pwd != '' &&
    //     this.form.usr != '' &&
    //     this.form.name != ''
    //   ) {
    //     let obj = this
    //     let params = new URLSearchParams()
    //     params.append('usr', obj.form.usr)
    //     params.append('pwd', obj.form.pwd)
    //     params.append('name', obj.form.name)

    //     axios({
    //       method: 'post',
    //       url: this.$hostname + 'user/update',
    //       data: params,
    //       headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    //     })
    //       .then(function(response) {
    //         if (response.data == 'True') {
    //           obj.$message({ message: '修改成功！', type: 'success' })
    //           obj.$emit('change')
    //         } else if (response.data == 'Taken') {
    //           obj.$message({ message: '用户名已占用', type: 'warning' })
    //           obj.form.usr = ''
    //         }
    //       })
    //       .catch(function() {
    //         obj.$message.error('糟糕，哪里出了点问题！')
    //       })
    //   } else {
    //     this.$message.error('请确认输入内容全部正确！')
    //   }
    // },
    LogOut: function() {
      let obj = this

      axios
        .get(this.$hostname + 'auth/logout')
        .then(function() {
          obj.$router.push('/auth')
          obj.$message('退出成功')
        })
        .catch(function() {
          obj.$message.error('糟糕，哪里出了点问题！')
        })
    },
  },
}
</script>
