import { createRouter, createWebHistory } from 'vue-router';
import Main from '../components/Main.vue';
import AddItem from '../components/AddItem.vue';
import EditItem from '../components/EditItem.vue';

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main,
  },
  {
    path: '/add',
    name: 'AddItem',
    component: AddItem, 
  },
  {
    path: '/edit/:id',
    name: 'EditItem',
    component: EditItem, // Make sure this is uncommented and properly imported
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
