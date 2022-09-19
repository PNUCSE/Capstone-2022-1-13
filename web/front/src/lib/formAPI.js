import axios from 'axios'

const baseUrl = 'http://164.125.252.182:8011'

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
        return response.data
    })
}

const formAPI = {
    postSubmit
};

export default formAPI;
