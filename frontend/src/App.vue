<template>
  <div>
    <div id="app">
      <navbar
        :isAuthenticated="isAuthenticated"
        :username="username"
        @logout="logout"
      />
      <router-view :updateAuthentication="updateAuthentication" />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar/NavbarPage.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
  data() {
    return {
      isAuthenticated: false,
      username: "",
    };
  },
  methods: {
    updateAuthentication({ isAuthenticated, username }) {
      this.isAuthenticated = isAuthenticated;
      this.username = username;
    },
    logout() {
      this.isAuthenticated = false;
      this.username = "";
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased; */
  /* -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
}
</style>
