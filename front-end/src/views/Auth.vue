<template>
  <div class="log">
    <div id="log-session">
      <div class="image">
        <img src="@/assets/log.jpeg" alt="log" />
      </div>
      <component :is="logview" @change="change"></component>
    </div>
  </div>
</template>

<script>
import Register from '@/components/Register.vue'
import SignIn from '@/components/SignIn.vue'

export default {
  name: 'Auth',
  data: () => ({
    logview: Register,
  }),
  components: {
    Register,
    SignIn,
  },
  methods: {
    change: function() {
      if (this.logview == Register) {
        this.logview = SignIn
      } else {
        this.logview = Register
      }
    },
  },
}
</script>

<style scoped>
#log-session {
  margin-top: 2%;
  margin-left: 7%;
  height: 600px;
  width: 1200px;
  background-color: rgb(218, 218, 218);
  box-shadow: 15px 15px 8px rgba(190, 190, 190, 0.1);
}
.image {
  float: left;
}
</style>
