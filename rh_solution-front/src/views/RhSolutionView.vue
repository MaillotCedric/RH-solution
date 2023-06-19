<template>
    <div id="rh-solution">
        <v-icon
            color="green-darken-2"
            class="my-2"
            @click="afficher_form_add()"
        >
            mdi-plus-circle-outline
        </v-icon>

        <v-table
            fixed-header
            height="500px"
        >
            <thead>
                <tr>
                    <th class="text-left"></th>
                    <th class="text-left">Prénom</th>
                    <th class="text-left">Nom</th>
                    <th class="text-left">Téléphone</th>
                    <th class="text-left">Email</th>
                    <th class="text-left"></th>
                    <th class="text-left"></th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="salarie in salaries"
                    :key="salarie['id']"
                >
                    <td>
                        <v-avatar
                            :color="salarie['genre'] === 'Male' ? 'indigo-darken-2' : salarie['genre'] === 'Female' ? 'pink-darken-2' : 'purple-darken-2'"
                            size="small"
                        >
                            <span class="text-h7">
                                {{ premier_caractere(salarie['prenom']) }}{{ premier_caractere(salarie['nom']) }}
                            </span>
                        </v-avatar>
                    </td>
                    <td>{{ salarie['prenom'] }}</td>
                    <td>{{ salarie['nom'] }}</td>
                    <td>{{ salarie['telephone'] }}</td>
                    <td>{{ salarie['email'] }}</td>
                    <td>
                        <v-icon
                            color="blue-darken-2"
                            @click="afficher_fiche(salarie['id'])"
                        >
                            mdi-eye-outline
                        </v-icon>
                    </td>
                    <td>
                        <v-icon
                            color="red-darken-2"
                            @click="afficher_warning(salarie['index'])"
                        >
                            mdi-delete-outline
                        </v-icon>
                    </td>
                </tr>
            </tbody>
        </v-table>

        <v-dialog
            v-model="dialog_visible"
            fullscreen
            :scrim="false"
            transition="dialog-bottom-transition"
        >
            <v-card>
                <v-toolbar
                    dark
                    :color="color"
                >
                    <v-btn
                        icon
                        dark
                        @click="dialog_visible = false"
                    >
                        <v-icon>mdi-close</v-icon>
                    </v-btn>
                    <v-toolbar-title>{{ dialog_title }}</v-toolbar-title>
                </v-toolbar>
            </v-card>
        </v-dialog>

        <v-dialog
            v-model="warning_visible"
            width="auto"
        >
            <v-card
                color="red-lighten-1"
            >
                <v-card-title>
                    Êtes vous sûr de vouloir supprimer
                </v-card-title>
                <v-card-text>
                    <div class="font-weight-bold text-h6">
                        {{ salaries[this.index_salarie]['prenom'] }}
                        {{ salaries[this.index_salarie]['nom'] }}
                    </div>
                </v-card-text>
                <v-card-actions>
                    <v-btn
                        variant="outlined"
                    >
                        <span
                            @click="supprimer_salarie()"
                        >Confirmer la suppression</span>
                    </v-btn>
                    <v-btn
                        variant="outlined"
                    >
                        <span
                            @click="warning_visible = false"
                        >Annuler</span>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>


        <v-dialog
            v-model="loading_visible"
            :scrim="false"
            persistent
            width="auto"
        >
            <v-card
                color="primary"
            >
                <v-card-text>
                Please stand by
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script lang="ts">
    export default {
        name: "rh-solution",
        data () {
            return {
                salaries: [],
                color: "",
                dialog_visible: false,
                warning_visible: false,
                loading_visible: false,
                dialog_title: ""
            }
        },
        methods: {
            get_salaries() {
                this.salaries.push(
                    {
                        id: 1,
                        index: 0,
                        nom: "LOVELACE",
                        prenom: "Ada",
                        telephone: "+33 692 12 34 56",
                        email: "al@example.com",
                        genre: "Femme",
                        email_personnel: "al.perso@example.com"
                    },
                    {
                        id: 2,
                        index: 1,
                        nom: "DOE",
                        prenom: "John",
                        telephone: "+33 692 78 91 01",
                        email: "jd@example.com",
                        genre: "Homme"
                    }
                )
            },
            premier_caractere(chaine_caracteres) {
                return chaine_caracteres.split("")[0]
            },
            afficher_form_add() {
                this.color = "green-darken-2"
                this.dialog_title = "Ajouter un nouveau salarié"
                this.dialog_visible = true
            },
            afficher_fiche(id_salarie) {
                let index_salarie = id_salarie - 1

                this.color = "blue-darken-2"
                this.dialog_title = this.salaries[index_salarie].prenom + " " + this.salaries[index_salarie].nom
                this.dialog_visible = true
            },
            afficher_warning(index_salarie) {
                this.warning_visible = true
            },
            supprimer_salarie() {
                this.warning_visible = false
                this.loading_visible = true
                setTimeout(() => (
                    this.salaries.splice(this.index_salarie, 1),
                    this.loading_visible = false
                ), 4000)
            }
        },
        created () {
            this.get_salaries()
        }
    }
</script>

<style scoped>
    @media (min-width: 1024px) {}
</style>
