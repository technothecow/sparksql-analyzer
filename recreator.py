from lark import Tree,Token

class Recreator:
    def __init__(self, tree: Tree):
        self.tree=tree.children[0]

    def recreate(self):
        if self.tree.data=='create_database_or_schema':
            creation_type=None
            if_not_exists=False
            name=None
            comment=None
            location=None
            properties=None
            for i in self.tree.children:
                if isinstance(i,Tree):
                    if i.data == 'ifnotexists_clause':
                        if_not_exists=True
                    elif i.data == 'comment_clause':
                        comment=i.children[0].value
                    elif i.data == 'location_clause':
                        location=i.children[0].value
                    elif i.data == 'properties_clause':
                        properties=list()
                        for j in i.children[0].children:
                            properties.append(f'j.children[0].value = j.children[1].value')
                        properties=', '.join(properties)
                elif i=='SCHEMA' or i=='DATABASE':
                    creation_type=i
                else:
                    name=i
            return f"""CREATE {creation_type}{' IF NOT EXISTS ' if if_not_exists else ' '}{name}
            {f"COMMENT {comment}" if comment is not None else ""}
            {f"LOCATION {location}" if location is not None else ""}
            {f"WITH DBPROPERTIES {properties}" if properties is not None else ""}"""
        else:
            raise Exception("That query can't be recreated!")