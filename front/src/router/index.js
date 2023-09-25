import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Register from '../views/RegisterPage.vue'
import Login from '../views/LoginPage.vue'
import PasswordPage from '../views/PasswordPage.vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
// import { faUser } from '@fortawesome/free-solid-svg-icons';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: Home
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: Register, FontAwesomeIcon // Utilisez la vue Register pour ce chemin
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: Login // Utilisez la vue Register pour ce chemin
  },
  {
    path: '/forgotPassword',
    name: 'forgotPasswordPage',
    component: PasswordPage // Utilisez la vue Register pour ce chemin
  }
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
