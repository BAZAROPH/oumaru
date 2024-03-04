// refreshToken function
async function refreshToken(endPoint){
    let refreshToken = sessionStorage.getItem('refreshToken');

    if(refreshToken){
        const body = {
            refresh: refreshToken
        }
        await axios.post(endPoint, body).then((response)=>{
            sessionStorage.setItem('accessToken', response.data.access)
        }).catch((error)=>{
            if(error.response.status === 401){
                // document.location.href = 'http://127.0.0.1:8003/astro/login';
                document.location.href('https://oumaru.com/astro/login');

            }
        })
    }else{
        console.log('hum')
        // document.location.href = 'http://127.0.0.1:8003/astro/login';
        document.location.href('https://oumaru.com/astro/login');
    }

}
refreshToken('https://oumaru.com/api/token/refresh');

function get(){
    const url = "https://oumaru.com/api/projects";
    const token = sessionStorage.getItem('accessToken');
    const config = {
    headers: {
        Authorization: `Bearer ${token}`,
    },
    };
    axios.get(url, config).then((response)=>{
        let devis = response.data;

        // console.log(clone.querySelector('#number').id)
        for(i=0; i < devis.length; i++){
            let tbody = document.getElementById('tbody');
            let tr = document.getElementById('tr');
            let clone = tr.cloneNode(true);
            
            //id row
            clone.querySelector('#number').textContent = devis[i].id;
            clone.querySelector('#number').id = `id-${devis[i].id}`;

            //last name row
            clone.querySelector('#last_name').textContent = devis[i].last_name;
            clone.querySelector('#last_name').id = `last_name-${devis[i].id}`;

            // first name row
            clone.querySelector('#first_name').textContent = devis[i].first_name;
            clone.querySelector('#first_name').id = `first_name-${devis[i].id}`;
            
            // email row
            clone.querySelector('#email').textContent = devis[i].email;
            clone.querySelector('#email').id = `email-${devis[i].id}`;

            //contact row
            clone.querySelector('#contact').textContent = devis[i].contact;
            clone.querySelector('#contact').id = `contact-${devis[i].id}`;

            // address row
            clone.querySelector('#address').textContent = devis[i].address;
            clone.querySelector('#address').id = `address-${devis[i].id}`;

            // date row
            clone.querySelector('#created_at').textContent = new Date(devis[i].created_at).toLocaleDateString();
            clone.querySelector('#created_at').id = `created_at-${devis[i].id}`;

            // setup status 
            if(devis[i].request_state === 0){
                clone.querySelector('#state').innerHTML = '<i class="bi bi-exclamation-diamond-fill text-warning"></i>';
            }else if(devis[i].state === 'danger'){
                clone.querySelector('#state').innerHTML = '<sapn class="bi bi-x-circle-fill text-danger">'
            }
            clone.querySelector('#state').id = `state-${devis[i].id}`;

            clone.querySelector('#see').id = `see-${devis[i].id}`;

            clone.querySelector('#delete').id = `delete-${devis[i].id}`;
            // console.log(number);
            tbody.appendChild(clone);
        }
        tr.remove();
    }).catch((error)=>{
        if(error.response.status === 401){
            refreshToken('https://oumaru.com/api/token/refresh');
            get();
        }
    });
}

get();
// let data = [
//     {
//         id: 1,
//         last_name: 'Coulibaly',
//         first_name: 'Cheick oumar',
//         email: 'bazaroph@gmail.com',
//         contact: '0141993677',
//         address: 'Cocody Faya',
//         state: 'success',
//         created_at: '21-12-2020'
//     },
//     {
//         id: 2,
//         last_name: 'Ouattara',
//         first_name: 'Mahama',
//         email: 'mahama@gmail.com',
//         contact: '0899273477',
//         address: 'Agnibilékrou, Plateau',
//         state: 'warning',
//         created_at: '21-12-2020'
//     },
//     {
//         id: 3,
//         last_name: 'Coulibaly',
//         first_name: 'Cheick oumar',
//         email: 'bazaroph@gmail.com',
//         contact: '0141993677',
//         address: 'Cocody Faya',
//         state: 'success',
//         created_at: '21-12-2021'
//     },
//     {
//         id: 4,
//         last_name: 'Drago',
//         first_name: 'Kall',
//         email: 'kadra@gmail.com',
//         contact: '0829266434',
//         address: 'Mar, Plateau',
//         state: 'danger',
//         created_at: '21-12-2022'
//     }
// ];