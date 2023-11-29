export default {
  props: ["isAuthenticated", "username"],
  data() {
    return {
      currentRoute: "",
    };
  },
  watch: {
    $route(to) {
      this.currentRoute = to.path;
    },
  },
  methods: {
    handleLogout() {
      this.$emit("logout");
    },
  },
};
