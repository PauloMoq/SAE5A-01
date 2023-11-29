import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./../pages/HomePage/HomePage.vue";
import Register from "./../pages/RegisterPage/RegisterPage.vue";
import Login from "../pages/LoginPage/LoginPage.vue";
import PasswordPage from "../pages/PasswordPage/PasswordPage.vue";
import SearchPage from "../pages/SearchPage/SearchPage.vue";
import HistoriquePage from "../pages/HistoriquePage/HistoriquePage.vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: Home,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: Register,
    FontAwesomeIcon,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: Login,
  },
  {
    path: "/forgotPassword",
    name: "forgotPasswordPage",
    component: PasswordPage,
  },
  {
    path: "/search",
    name: "SearchPage",
    component: SearchPage,
  },
  {
    path: "/historique",
    name: "HistoriquePage",
    component: HistoriquePage,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
