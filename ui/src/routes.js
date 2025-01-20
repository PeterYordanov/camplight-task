import Home from './pages/Home'
import About from './pages/About'

export const routes = {
  home: {
    name: 'Home',
    path: '/',
    component: <Home />
  },
  about: {
    name: 'About',
    path: '/about',
    component: <About />
  }
}
