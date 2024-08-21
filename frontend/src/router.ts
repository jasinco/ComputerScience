import { createWebHashHistory, createRouter } from "vue-router";

import landing_page from "./components/landing_page.vue";

const routes = [{ path: "/", component: landing_page }];
export default createRouter({
  history: createWebHashHistory(),
  routes,
});
