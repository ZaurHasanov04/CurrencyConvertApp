<template>
    <v-container>
      <v-row class="mb-3 mt-5">
        <v-col cols="4"></v-col>
        <v-col cols="4">
          <v-card ref="form" lazy-validation class="text-center">
            <v-card-title> Register Form </v-card-title>
            <v-card-text>
              <v-text-field
                v-model="newUser.username"
                label="Username"
                outlined
                required
              ></v-text-field>
  
              <v-text-field
                v-model="newUser.email"
                label="Email"
                outlined
              ></v-text-field>
  
              <v-text-field
                v-model="newUser.password1"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                
                hint="At least 8 characters"
                label="Password"
                counter
                @click:append="show1 = !show1"
                outlined
              ></v-text-field>
  
              <v-text-field
                v-model="newUser.password2"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show2 ? 'text' : 'password'"
                
                hint="At least 8 characters"
                label="Repeat Password"
                counter
                @click:append="show2 = !show2"
                outlined
              ></v-text-field>
  
              <v-btn class="mr-4" @click="reset">Clear</v-btn>
              <v-btn
                color="success"
                :disabled="
                  !newUser.username || !newUser.password1 || !newUser.password2
                "
                @click="register"
              >
                Register
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="4"></v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";

  export default {
    name: "SignUp",
  
    data: () => ({
      show1: false,
      show2: false,
      newUser: {
        username: "",
        email: "",
        password1: "",
        password2: "",
        
      },
      // passwordRules: [
      //   (v) => !!v || "Password is required",
      //   (v) => (v && v.length >= 8) || "Password must be atleast 8 characters",
      // ],
      url: "http://127.0.0.1:8000/user/",
    }),
    methods: {
      reset() {
        this.$refs.form.reset();
      },
      register() {
        var data = {
          username: this.newUser.username,
          email: this.newUser.email,
          password_first: this.newUser.password1,
          password_second: this.newUser.password2,
        };

        console.log(data)
        axios.post(this.url, data).then((response) => {
          console.log(response.data);
          var id = response.data.id;
          this.$router.push({ name: "VerifyOTP", params: { userId: id } });
        })
        .catch(error =>{
          console.log(error.response)
          console.error('Error:', error.response.data);
        });
      },
    },
  };
  </script>