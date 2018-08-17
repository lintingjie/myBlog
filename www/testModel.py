import asyncio

from www import orm
from www.models import User


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='test1', email='test1@test.com', passwd='test', image='about:blank')
    await u.save()
    await orm.destory_pool()


async def find(loop):
    await orm.create_pool(loop, user='root', password='root', db='awesome')
    rs = await User.findAll()
    print('查找测试： %s, size=%s' % (rs, len(rs)))
    await orm.destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

# async def test(loop):
#     await orm.create_pool(loop=loop, user='root', password='root', db='awesome')
#     u = User(name='test22', email='test22@test.com', passwd='test', image='about:blank')
#     await u.save()
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([test(loop)]))
#     loop.close()
