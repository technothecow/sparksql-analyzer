from lark import Tree, Token


class Recreator:
    def __init__(self, tree: Tree):
        self.tree = tree.children[0]

    def recreate(self):
        if self.tree.data == 'create_database_or_schema':
            creation_type = None
            if_not_exists = False
            name = None
            comment = None
            location = None
            properties = None
            for i in self.tree.children:
                if isinstance(i, Tree):
                    if i.data == 'ifnotexists_clause':
                        if_not_exists = True
                    elif i.data == 'comment_clause':
                        comment = i.children[0].value
                    elif i.data == 'location_clause':
                        location = i.children[0].value
                    elif i.data == 'properties_clause':
                        properties = list()
                        for j in i.children[0].children:
                            properties.append(f'{j.children[0].value} = {j.children[1].value}')
                        properties = ', '.join(properties)
                elif i == 'SCHEMA' or i == 'DATABASE':
                    creation_type = i
                else:
                    name = i
            result = list()
            result.append(f"CREATE {creation_type}{' IF NOT EXISTS ' if if_not_exists else ' '}{name}")
            if comment is not None:
                result.append(f"\tCOMMENT {comment}")
            if location is not None:
                result.append(f"\tLOCATION {location}")
            if properties is not None:
                result.append(f"\tWITH DBPROPERTIES ({properties})")
            return '\n'.join(result)
        else:
            raise Exception("Given query can't be recreated!")
