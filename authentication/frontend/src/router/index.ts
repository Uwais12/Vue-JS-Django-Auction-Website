import { createWebHistory, createRouter } from "vue-router";
import Profile from '../views/Profile.vue'
import Shop from '../views/Shop.vue'
const Home = { template: '<div>Home</div>' }

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
    },
    {
        path: '/shop',
        name: 'Shop',
        component: Shop,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;

