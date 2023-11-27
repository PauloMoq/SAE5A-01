import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Register from '../views/RegisterPage.vue'
import Login from '../views/LoginPage.vue'
import PasswordPage from '../views/PasswordPage.vue'
import SearchPage from '../views/SearchPage.vue'
import HistoriquePage from '../views/HistoriquePage.vue'


import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

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
    component: Login // Utilisez la vue Login pour ce chemin
  },
  {
    path: '/forgotPassword',
    name: 'forgotPasswordPage',
    component: PasswordPage // Utilisez la vue PasswordPage pour ce chemin
  },
  {
    path: '/search',
    name: 'SearchPage',
    component: SearchPage // Utilisez la vue SearchPage pour ce chemin
  },
  {
    path: '/historique',
    name: 'HistoriquePage',
    component: HistoriquePage // Utilisez la vue SearchPage pour ce chemin
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
