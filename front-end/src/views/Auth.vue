<template>
  <div class="log">
    <div id="log-session">
      <img class="image" src="@/assets/log.png" alt="log" />
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
  margin-top: 3%;
  margin-left: 7%;
  height: 600px;
  width: 1200px;
  background-color: rgb(235, 235, 235);
  box-shadow: 15px 15px 8px rgba(190, 190, 190, 0.1);
}
.image {
  float: left;
  height: 600px;
}
</style>
