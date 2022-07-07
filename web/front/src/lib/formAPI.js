import axios from 'axios'

const baseUrl = 'http://127.0.0.1:8000'

const headers = {
    'Accept': 'application/json',
    'Content-Type': 'multipart/form-data',
};

const postSubmit = async(video, logo) => {
    return await axios.post(`${baseUrl}/logo/`, {
        image: logo,
        video: video
    }, {
        headers: headers
    })
    .then(response => {
        console.log(response)
        return response.data
    })
}

const formAPI = {
    postSubmit
};

export default formAPI;