typedef struct _node {
    int           label;
    int           type;
    char          *name;
    int           ival;
    float         fval;
    struct _node *left;
    struct _node *right;
} node;

enum {TINT, TFLOAT };
