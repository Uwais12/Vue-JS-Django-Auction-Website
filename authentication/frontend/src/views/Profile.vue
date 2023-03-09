<template>

    <li class="list-group-item border border-2 mb-3">
        <p class="display-5 border rounded border-4"><strong>{{ username }}</strong></p>

        <p class="h5">{{ profile.email }}</p>
        <p class="h5"><img :src="'http://localhost:8000' + profile.profile_picture" /></p>

        <p v-if="profile.date_of_birth != null" class="h5">Date of birth: {{ profile.date_of_birth }}</p>
    </li>

    <!-- Form to change the details of the user  -->
    <button @click="showEditProfile()">Edit Profile</button>

    <div style="display: none;" class=" border rounded bg-secondary shadow p-4 mb-4" id="editProfileForm">
        <p class="h1 mb-4">Edit your details</p>
        <form id="updateProfileForm" @submit.prevent method="POST">
            <div class="form-group">
                <label for="username">Change your username</label><br><br>

                <input class="form-control" type="text" name="username" id="username" placeholder="Change your username"
                    :value=username /><br>
                <label for="email">Change your email</label><br><br>

                <input class="form-control" type="email" name="email" id="email" placeholder="Change your email"
                    :value=profile.email /><br>
                <label for="date">Change your date of birth</label><br><br>
                <input class="form-control" type="date" name="date_of_birth" id="date_of_birth"
                    :value=profile.date_of_birth /><br><br>
                <label for="profile_picture">Change your profile picture</label><br><br>
                <input class="form-control-image" type="file" name="profile_picture" id="profile_picture"
                    accept="image/png, image/jpeg, image/jpg" placeholder="Change profile picture" /><br>

                <div class="row justify-content-center">
                    <button type="submit" @click="edit_profile()"
                        class="btn btn-primary btn-lg d-flex justify-content-center mt-3">Edit</button>
                </div>
            </div>
        </form>
    </div>

</template>


<script lang="ts">

import { defineComponent } from 'vue';

import 'bootstrap/dist/css/bootstrap.css';
import { text } from 'body-parser';

type Profile = {
    id: number,
    email: string;
    date_of_birth: Date;
    profile_picture: string;
}

export default defineComponent({

    mounted() {
        let script1 = document.createElement('script')
        script1.setAttribute('src', 'https://unpkg.com/vue@3')
        document.head.appendChild(script1)

        let script2 = document.createElement('script')
        script2.setAttribute('src', 'https://unpkg.com/vue-router@4')
        document.head.appendChild(script2)

        this.get_profile_details();
    },

    data() {
        return {
            profile: {} as Profile,
            username: '',
        };
    },

    methods: {

        showEditProfile() {
            let form1 = document.getElementById('editProfileForm') as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },

        async get_profile_details() {
            let response = await fetch("http://localhost:8000/api/profile", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            if (response.ok) {
                let data = await response.json();
                if (data.logged_in == false) {
                    window.location.href = 'http://localhost:8000/login/';
                }
                this.username = data.username;
                this.profile = data.profile;
                console.log(this.profile)
            }
            else {
                alert("Connection lost...")
            }
        },

        async edit_profile() {
            /*
            Method to edit the profile
            It uses an Ajax request to send the new details of the team to be handled by the backend
            */
            let updateProfile = document.getElementById('updateProfileForm') as HTMLFormElement;
            let formData: FormData = new FormData(updateProfile)
            console.log(formData)
            var input = document.getElementById('profile_picture') as HTMLFormElement
            var inputusername = document.getElementById('username') as HTMLFormElement
            var email = document.getElementById('email') as HTMLFormElement
            var dob = document.getElementById('date_of_birth') as HTMLFormElement


            formData.append('profile_picture', input.files[0])
            // formData.append('username', inputusername)
            // formData.append('email', email.value)
            // formData.append('dob', dob.value)


            console.log(input.files)
            let response = await fetch("http://localhost:8000/api/profile/" + this.profile.id, {
                method: "PUT",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",

                body: formData
            });
            if (response.ok) {
                // send the response
                let data = await response.json();
                this.username = data.username;
                this.profile = data.profile;
                this.showEditProfile()

            }
            else {
                alert("Profile could not be edited...")
            }
        },
    }
})

</script>