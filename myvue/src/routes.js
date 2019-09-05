import AppHeader from './components/AppHeader'
import TourDetail from './components/TourDetail'
import TaskDetails from './components/TaskDetails'
import NoteList from './components/NoteList'
import Login    from './components/Login'

export const routes = [
    {
        path: '/',
        name: 'note-list',
        component: NoteList
      },
      {
        path: '/tour',
        name: 'notelist',
        component: NoteList
      },
      { 
        path: '/detail/:id',
        name: 'tourdetail',
        props: true,
        component: TourDetail
      },
      {
        path:'/details',
        name: 'tourdetails',
        component: TaskDetails
      },
      {
        path: '/login',
        name: 'login',
        component: Login
      },
      { path: '*', component:() => import('./components/NoteList.vue')}
]