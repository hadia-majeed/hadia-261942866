
            self.bullet_lst.append(bullet)
            self.slow_down_counter = 1
        

    def bulletmovements(self,vel,objp): #overrideing methods from the ship class
        self.slowdownz()
        for i in self.bullet_lst:
            i.move(vel)
            if i.out_screen(height):
                self.bullet_lst.remove(i)
            else:
                for obj in objp:
                    if  i.collision(obj):