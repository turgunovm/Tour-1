import { HTTP } from './common'
export const Note = {
  create (config) {
    return HTTP.post('/tourpack/', config).then(response => {
      return response.data
    })
  },
  delete (note) {
    return HTTP.delete(`/tourpack/${note.id}/`)
  },
  list () {
    return HTTP.get('/tourpack/').then(response => {
      return response.data
    })
  },
  detail(note) {
    return HTTP.get('/tourpack/${note.id}/').then(response =>{
      return response.data
       
    })
  }
}