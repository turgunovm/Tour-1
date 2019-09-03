import AppHeader from './components/AppHeader'
import TourDetail from './components/TourDetail'
import TaskDetails from './components/TaskDetails'
import NoteList from './components/NoteList'
import Login    from './components/Login'

export const routes = [
    {
        path: '/',
        name: 'AppHeader',
        component: AppHeader
      },
      {
        path: '/tour',
        name: 'notelist',
        component: NoteList
      },
      {
        path: true,
        path: '/detail/:tour_id',
        name: 'tourdetail',
        component: TourDetail
      },
      {
        path: true,
        path: '/details/:note_id',
        name: 'tourdetails',
        component: TaskDetails
      },
      {
       
        path: '/login',
        name: 'login',
        component: Login
      },
      { path: '*', component:() => import('./components/AppHeader.vue')}
]