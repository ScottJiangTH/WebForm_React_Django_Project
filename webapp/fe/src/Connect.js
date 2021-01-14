import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class Connect{
    constructor(){}
    
    getCourses(){
        const url = `${API_URL}/api/courses`;
        return axios.get(url).then(response => response.data);
    }
    getCourse(courseNumber){
        const url = `${API_URL}/api/courses/${courseNumber}`;
        return axios.get(url).then(response => response.data);
    }
    createCourse(course){
        const url = `${API_URL}/api/courses`;
        return axios.post(url,course);
    }
    deleteCourse(course){
        const url = `${API_URL}/api/courses/${course.courseNumber}`;
        return axios.delete(url);
    }
}