#include <stdlib.h>

#include "quadtree.h"

/********************************************************************/
/* NOM : Barbe                                                           */
/* PRENOM : Mathieu                                                         */
/* NOM DE MACHINE :                                                 */
/*                                                                  */
/* Les fonctions ci-dessous pointent initialement sur une solution  */
/* fournie par les enseignants via le module helper.o               */
/* MAIS : ces fonctions sont a re-implementer integralement en      */
/* remplacant le code fourni par votre propre code                  */
/* Il s'agit de VOTRE TRAVAIL A EFFECTUER                           */
/********************************************************************/

/*
   TODO : print_picture

   Affiche a l'ecran le message texte <message> passe en parametre
   suivi de l'image picture sous forme texte (des 0 et des 1
   uniquement, ligne par ligne de l'image avec un saut entre chaque
   ligne et un espace entre les 0 et 1 de chaque ligne).

   Indice : format %hhu pour afficher des donnees de type uint8_t
 */

void fonction_1(char *message, struct picture *p)
{
    /* Ligne ci-dessous a commenter et a remplacer par votre propre
     * implementation!  (ou bien a conserver en cas de soucis pour
     * ecrire cette fonction)
     */
    //print_picture_teacher(message, p);
    printf("%s\n", message);
    // boucle sur les ligne
    for(size_t i=0; i<p->side_size; i++){
       // boucle sur les pixels
       for(size_t j=0; j< p->side_size; j++){
          printf("%hhu ", p->pixels[i+ j* p->side_size]);
       } // end for
       printf("\n");
    } // end for
    
} // end def

/*
   TODO : create_node

   Alloue un quadtree et initialise les champs side_size et color avec
   les valeurs passees en parametre. Les champs nw, ne, sw, se sont a
   initialiser avec un pointeur NULL.

   NOTA BENE : il est fortement recommande d'utiliser cette fonction
   pour implementer la fonction convert_picture_to_tree().
*/


struct arbre boulot(int a){

struct quadtree *fonction2_with_poiteur(uint16_t side_size, enum node_color color)
{
   struct quadtree *q = malloc(sizeof(struct quadtree));
   q->side_size = side_size;
   q->color = color;
   q->nw = q->ne = q->sw = q->se = NULL;
   return q;
} // end def

/* TODO : is_uniform_color

   Retourne true si tous les pixels de la region d'image definie par
   les parametres sont de la meme couleur. La region d'image a tester
   est un carre defini par son point superieur gauche de coordonnees x
   et y et la taille du cote du carre side_size_area. Cette region
   ainsi definie est une partition de l'image p passee en parametre.

   NOTA BENE : il est fortement recommande d'utiliser cette fonction
   pour implementer la fonction convert_picture_to_tree().
*/

void *  fonction3(){

